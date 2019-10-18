from myservice.classes.quiz import Quiz, Answer, Question, NonExistingAnswerError, LostQuizError, CompletedQuizError
import unittest


class TestQuiz(unittest.TestCase):
    # Test Answer
    def test_serialize(self):
        ans = Answer('a', 1)
        res = ans.serialize()
        self.assertEqual(res, {'answer': 'a'})

    # Test Question
    def test_question_checkAnswer_correct(self):
        quest = 'q?'
        ans = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        question = Question(quest, ans)
        given_answer = 'a'
        res = question.checkAnswer(given_answer)
        self.assertEqual(res, 1)

    def test_question_checkAnswer_nonexisting(self):
        quest = 'q?'
        ans = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        question = Question(quest, ans)
        given_answer = 'd'
        self.assertRaises(NonExistingAnswerError, question.checkAnswer, given_answer)

    def test_question_checkAnswer_wrong(self):
        quest = 'q?'
        ans = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        question = Question(quest, ans)
        res = question.checkAnswer('b')
        self.assertEqual(res, 0)

    #Test Quiz
    def test_quiz_iscompleted(self):
        quest = 'q?'
        ans = []
        questions = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        questions.append(Question(quest, ans))
        questions.append(Question(quest, ans))
        quiz = Quiz(0, questions)

        quiz.checkAnswer('a')
        self.assertFalse(quiz.isCompleted())

        try:
            quiz.checkAnswer('a')
        except CompletedQuizError:
            self.assertTrue(quiz.isCompleted())

    def test_quiz_islost(self):
        quest = 'q?'
        ans = []
        questions = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        questions.append(Question(quest, ans))
        questions.append(Question(quest, ans))
        quiz = Quiz(0, questions)
        quiz.checkAnswer('a')
        self.assertEqual(quiz.currentQuestion, 1)
        try:
            quiz.checkAnswer('b')
        except LostQuizError:
            self.assertEqual(quiz.currentQuestion, -1)


    def test_quiz_checkAnswer_correct(self):
        quest = 'q?'
        ans = []
        questions = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        questions.append(Question(quest, ans))
        questions.append(Question(quest, ans))
        questions.append(Question(quest, ans))

        quiz = Quiz(0, questions)
        res = quiz.checkAnswer('a')
        self.assertEqual(res, 1)
        res = quiz.checkAnswer('a')
        self.assertEqual(res, 2)

    def test_quiz_checkAnswer_wrong(self):
        quest = 'q?'
        ans = []
        questions = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        questions.append(Question(quest, ans))

        quiz = Quiz(0, questions)
        self.assertRaises(LostQuizError, quiz.checkAnswer, 'b')

    def test_quiz_checkAnswer_complete(self):
        quest = 'q?'
        ans = []
        questions = []
        ans.append(Answer('a', 1))
        ans.append(Answer('b', 0))
        ans.append(Answer('c', 0))
        questions.append(Question(quest, ans))

        quiz = Quiz(0, questions)
        self.assertRaises(CompletedQuizError, quiz.checkAnswer, 'a')


if __name__ == '__main__':
    unittest.main()
