from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question, Choice
from django.urls import reverse


def create_question(q_txt, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(q_txt=q_txt, pub_date=time)


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published(), False)

    def test_was_published_recently_with_past_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published(), True)

    def test_was_published_with_choice(self):
        question = create_question('Test question with choice.', days=-5)
        question.choice_set.create(choice_txt='Vote for this', votes=0)
        self.assertIs(question.was_published(), True)

    def test_was_published_with_no_choice(self):
        question = create_question('Test question with no choice.', days=-5)
        self.assertIs(question.was_published(), False)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls area available.')
        self.assertQuerysetEqual(response.context['latest_questions_list'], [])

    def test_past_question(self):
        question = create_question(q_txt='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions_list'], [question])

    def test_future_question(self):
        create_question(q_txt='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(
            response.context(['latest_questions_list'], []))

    def test_future_question_and_past_question(self):
        question = create_question(q_txt='Past question.', days=-30)
        create_question(q_txt='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions_list'], [question])

    def test_two_past_questions(self):
        question1 = create_question(q_txt='Past question 1.', days=-30)
        question2 = create_question(q_txt='Past question 2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_questions_list'],
                                 [question1, question2])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(q_txt='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(q_txt='Past question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.q_txt)


class QuestionResultsViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(q_txt='Future question.', days=5)
        url = reverse('polls:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(q_txt='Past question.', days=-5)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.q_txt)
# Create your tests here.
