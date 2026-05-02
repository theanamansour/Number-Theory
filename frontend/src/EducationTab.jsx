import { useEffect, useMemo, useState } from "react";
import {
  BookOpen,
  Zap,
  HelpCircle,
  CheckCircle,
  XCircle,
  Lightbulb,
  ArrowRight,
  ArrowLeft,
  Trophy,
  BarChart3,
  GraduationCap,
  CircleHelp,
  Hash,
  Grid2X2,
  Diamond,
} from "lucide-react";

const BACKEND_BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
const API_BASE = `${BACKEND_BASE}/api/education`;

const MODULE_CONFIG = {
  factorization: {
    id: "factorization",
    title: "Prime Factorization",
    description: "Decompose integers into products of primes.",
    icon: <Hash size={28} strokeWidth={1.8} />,
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 10,
    accent: "purple",
    lessons: [
      "What is a prime number?",
      "Prime factorization idea",
      "Repeated division method",
      "Worked examples",
    ],
  },

  totient: {
    id: "totient",
    title: "Euler Totient",
    description: "Explore Euler’s totient function φ(n).",
    icon: "φ",
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 10,
    accent: "purple",
    lessons: [
      "Introduction to φ(n)",
      "Reduced residue sets",
      "Computing φ(n)",
      "Worked examples",
    ],
  },

  fastexp: {
    id: "fastexp",
    title: "Fast Exponentiation",
    description: "Compute large powers efficiently.",
    icon: <Zap size={30} strokeWidth={1.8} />,
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 10,
    accent: "purple",
    lessons: [
      "Why fast exponentiation?",
      "Repeated squaring",
      "Binary exponentiation",
      "Modular examples",
    ],
  },

  millerrabin: {
    id: "millerrabin",
    title: "Miller–Rabin",
    description: "Probabilistic primality testing algorithm.",
    icon: <Diamond size={27} strokeWidth={1.8} />,
    lessonsTotal: 5,
    practiceTotal: 6,
    quizTotal: 10,
    accent: "purple",
    lessons: [
      "Primality testing",
      "Writing n − 1 = 2ᵏq",
      "Witnesses",
      "Maybe prime vs composite",
      "Worked examples",
    ],
  },

  crt: {
    id: "crt",
    title: "Chinese Remainder Theorem",
    description: "Solve systems of congruences efficiently.",
    icon: <Grid2X2 size={28} strokeWidth={1.8} />,
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 10,
    accent: "purple",
    lessons: [
      "CRT intuition",
      "Pairwise coprime moduli",
      "Recovering A from residues",
      "Worked examples",
    ],
  },
};

function EducationTab({ user, openAuthModal }) {
  const [selectedModuleId, setSelectedModuleId] = useState(null);
  const [activeModuleTab, setActiveModuleTab] = useState("lessons");
  const [openedLesson, setOpenedLesson] = useState(null);

  const [completedLessons, setCompletedLessons] = useState({});
  const [completedPractice, setCompletedPractice] = useState({});

  const [lesson, setLesson] = useState(null);
  const [practice, setPractice] = useState([]);
  const [quiz, setQuiz] = useState([]);

  const [practiceResults, setPracticeResults] = useState({});
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizResult, setQuizResult] = useState(null);

  const [progressRows, setProgressRows] = useState([]);
  const [error, setError] = useState("");

  const selectedModule = selectedModuleId ? MODULE_CONFIG[selectedModuleId] : null;

  async function fetchJSON(url, options = {}) {
    const response = await fetch(url, options);
    const data = await response.json();

    if (!response.ok) {
      throw new Error(
        data?.detail || data?.error?.message || "Something went wrong."
      );
    }

    return data;
  }

  function getAuthHeaders() {
    const token = localStorage.getItem("token");

    if (!token) {
      return {};
    }

    return {
      Authorization: `Bearer ${token}`,
    };
  }

  useEffect(() => {
    loadProgress();
  }, [user]);

  async function loadProgress() {
    try {
      setError("");

      if (!user) {
        setProgressRows([]);
        return;
      }

      const progressData = await fetchJSON(`${API_BASE}/progress/me`, {
        headers: {
          ...getAuthHeaders(),
        },
      });

      setProgressRows(progressData.progress || []);
    } catch (err) {
      setError(err.message);
    }
  }

  async function openModule(moduleId) {
    try {
      setError("");
      setSelectedModuleId(moduleId);
      setActiveModuleTab("lessons");
      setOpenedLesson(null);

      setPracticeResults({});
      setQuizAnswers({});
      setQuizResult(null);

      const lessonData = await fetchJSON(`${API_BASE}/topics/${moduleId}`);
      const practiceData = await fetchJSON(`${API_BASE}/practice/${moduleId}`);
      const quizData = await fetchJSON(`${API_BASE}/quiz/${moduleId}`);

      setLesson(lessonData);
      setPractice(practiceData.practice || []);
      setQuiz(quizData.questions || []);
    } catch (err) {
      setError(err.message);
    }
  }

  function goBackToModules() {
    setSelectedModuleId(null);
    setActiveModuleTab("lessons");
    setOpenedLesson(null);

    setLesson(null);
    setPractice([]);
    setQuiz([]);

    setPracticeResults({});
    setQuizAnswers({});
    setQuizResult(null);
  }

  async function markLessonCompleted(moduleId, lessonId) {
    setCompletedLessons((previous) => ({
      ...previous,
      [moduleId]: {
        ...(previous[moduleId] || {}),
        [lessonId]: true,
      },
    }));

    setOpenedLesson(null);

    if (!user) {
      return;
    }

    try {
      await fetchJSON(`${API_BASE}/lesson/complete`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...getAuthHeaders(),
        },
        body: JSON.stringify({
          topic_id: moduleId,
          lesson_id: lessonId,
        }),
      });

      await loadProgress();
    } catch (err) {
      setError(err.message);
    }
  }

  function getCompletedLessonsForModule(moduleId) {
    const savedLessons = {};

    progressRows
      .filter(
        (row) =>
          row.topic_id === moduleId &&
          row.mode === "lesson" &&
          row.is_correct
      )
      .forEach((row) => {
        savedLessons[row.item_id] = true;
      });

    const localLessons = completedLessons[moduleId] || {};

    return {
      ...savedLessons,
      ...localLessons,
    };
  }

  function getCompletedPracticeForModule(moduleId) {
    const savedPractice = {};

    progressRows
      .filter(
        (row) =>
          row.topic_id === moduleId &&
          row.mode === "practice" &&
          row.is_correct
      )
      .forEach((row) => {
        savedPractice[row.item_id] = true;
      });

    const localPractice = completedPractice[moduleId] || {};

    return {
      ...savedPractice,
      ...localPractice,
    };
  }

  function getQuizStatusForModule(moduleId) {
    const quizRows = progressRows.filter(
      (row) => row.topic_id === moduleId && row.mode === "quiz" && row.total
    );

    const bestScore = quizRows.reduce((best, row) => {
      const percentage = Math.round((row.score / row.total) * 100);
      return Math.max(best, percentage);
    }, 0);

    return {
      completed: quizRows.length > 0,
      attempts: quizRows.length,
      bestScore,
    };
  }

  function getModuleProgress(moduleId) {
    const config = MODULE_CONFIG[moduleId];

    const moduleRows = progressRows.filter((row) => row.topic_id === moduleId);

    const savedLessons = new Set(
      moduleRows
        .filter((row) => row.mode === "lesson" && row.is_correct)
        .map((row) => row.item_id)
    );

    const localLessons = completedLessons[moduleId] || {};
    Object.keys(localLessons).forEach((lessonId) => {
      savedLessons.add(lessonId);
    });

    const savedPractice = new Set(
      moduleRows
        .filter((row) => row.mode === "practice" && row.is_correct)
        .map((row) => row.item_id)
    );

    const localPractice = completedPractice[moduleId] || {};
    Object.keys(localPractice).forEach((exerciseId) => {
      savedPractice.add(exerciseId);
    });

    const bestQuizPercentage = moduleRows
      .filter((row) => row.mode === "quiz" && row.total)
      .reduce((best, row) => {
        const percentage = Math.round((row.score / row.total) * 100);
        return Math.max(best, percentage);
      }, 0);

    const lessonsCompleted = Math.min(savedLessons.size, config.lessonsTotal);
    const practiceCompleted = Math.min(savedPractice.size, config.practiceTotal);

    const quizzesCompleted = bestQuizPercentage > 0 ? 1 : 0;

    const lessonPercent =
      config.lessonsTotal > 0
        ? Math.round((lessonsCompleted / config.lessonsTotal) * 100)
        : 0;

    const practicePercent =
      config.practiceTotal > 0
        ? Math.round((practiceCompleted / config.practiceTotal) * 100)
        : 0;

    const quizCompletionPercent = quizzesCompleted > 0 ? 100 : 0;
    const quizScorePercent = bestQuizPercentage;

    const percentage = Math.round(
      lessonPercent * 0.35 +
        practicePercent * 0.4 +
        quizScorePercent * 0.25
    );

    return {
      lessonsCompleted,
      practiceCompleted,
      quizzesCompleted,
      quizScore: bestQuizPercentage,

      lessonPercent,
      practicePercent,
      quizCompletionPercent,
      quizScorePercent,
      percentage,
    };
  }

  const overallProgress = useMemo(() => {
    const moduleIds = Object.keys(MODULE_CONFIG);

    const modulePercentages = moduleIds.map(
      (moduleId) => getModuleProgress(moduleId).percentage
    );

    const overall =
      modulePercentages.length > 0
        ? Math.round(
            modulePercentages.reduce((sum, value) => sum + value, 0) /
              modulePercentages.length
          )
        : 0;

    const lessonsCompleted = moduleIds.reduce(
      (sum, moduleId) => sum + getModuleProgress(moduleId).lessonsCompleted,
      0
    );

    const practiceCompleted = moduleIds.reduce(
      (sum, moduleId) => sum + getModuleProgress(moduleId).practiceCompleted,
      0
    );

    const quizzesCompleted = moduleIds.reduce(
      (sum, moduleId) => sum + getModuleProgress(moduleId).quizzesCompleted,
      0
    );

    const totalLessons = moduleIds.reduce(
      (sum, moduleId) => sum + MODULE_CONFIG[moduleId].lessonsTotal,
      0
    );

    const totalPractice = moduleIds.reduce(
      (sum, moduleId) => sum + MODULE_CONFIG[moduleId].practiceTotal,
      0
    );

    const totalQuizzes = moduleIds.length;

    const lessonPercent =
      totalLessons > 0
        ? Math.round((lessonsCompleted / totalLessons) * 100)
        : 0;

    const practicePercent =
      totalPractice > 0
        ? Math.round((practiceCompleted / totalPractice) * 100)
        : 0;

    const quizCompletionPercent =
      totalQuizzes > 0
        ? Math.round((quizzesCompleted / totalQuizzes) * 100)
        : 0;

    const averageQuizScore =
      moduleIds.length > 0
        ? Math.round(
            moduleIds.reduce(
              (sum, moduleId) => sum + getModuleProgress(moduleId).quizScore,
              0
            ) / moduleIds.length
          )
        : 0;

    return {
      overall,
      lessonsCompleted,
      practiceCompleted,
      quizzesCompleted,
      totalLessons,
      totalPractice,
      totalQuizzes,
      lessonPercent,
      practicePercent,
      quizCompletionPercent,
      averageQuizScore,
    };
  }, [progressRows, completedLessons, completedPractice]);

  async function checkPractice(exerciseId, stepId, answer) {
    try {
      setError("");

      const result = await fetchJSON(`${API_BASE}/practice/check`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...getAuthHeaders(),
        },
        body: JSON.stringify({
          topic_id: selectedModuleId,
          exercise_id: exerciseId,
          step_id: stepId,
          answer,
        }),
      });

      const resultKey = `${exerciseId}:${stepId}`;

      setPracticeResults((previous) => ({
        ...previous,
        [resultKey]: result,
      }));

      if (result.is_correct && result.is_final_step) {
        setCompletedPractice((previous) => ({
          ...previous,
          [selectedModuleId]: {
            ...(previous[selectedModuleId] || {}),
            [exerciseId]: true,
          },
        }));
      }

      await loadProgress();

      return result;
    } catch (err) {
      setError(err.message);
      return null;
    }
  }

  function clearPracticeResults(exerciseId) {
    setPracticeResults((previous) => {
      const next = { ...previous };

      Object.keys(next).forEach((key) => {
        if (key.startsWith(`${exerciseId}:`)) {
          delete next[key];
        }
      });

      return next;
    });
  }

  async function submitQuiz() {
    try {
      setError("");

      const answers = quiz.map((question) => {
        if (question.type === "input") {
          return {
            question_id: question.id,
            answer: quizAnswers[question.id] || "",
          };
        }

        return {
          question_id: question.id,
          selected_option_id: quizAnswers[question.id] || "",
        };
      });

      const result = await fetchJSON(`${API_BASE}/quiz/check`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...getAuthHeaders(),
        },
        body: JSON.stringify({
          topic_id: selectedModuleId,
          answers,
        }),
      });

      setQuizResult(result);
      await loadProgress();
    } catch (err) {
      setError(err.message);
    }
  }

  function redoQuiz() {
    setQuizAnswers({});
    setQuizResult(null);
  }

  if (selectedModule) {
    const moduleProgress = getModuleProgress(selectedModule.id);
    const quizStatus = getQuizStatusForModule(selectedModule.id);

    return (
      <section className="education-v2">
        {error && <div className="error">{error}</div>}

        <button
          type="button"
          className="education-back-button"
          onClick={goBackToModules}
        >
          <ArrowLeft size={16} />
          Back to Modules
        </button>

        {!user && <SaveProgressNote openAuthModal={openAuthModal} />}

        <div className="education-main-grid">
          <main className="education-modules-area">
            <div className="module-detail-hero">
              <div className={`module-detail-icon ${selectedModule.accent}`}>
                {selectedModule.icon}
              </div>

              <div className="module-detail-info">
                <h2>{selectedModule.title}</h2>
                <p>{selectedModule.description}</p>
              </div>

              <div className="module-detail-stats">
                <MiniStat
                  icon={<BookOpen size={18} />}
                  label="Lessons"
                  value={selectedModule.lessonsTotal}
                />

                <MiniStat
                  icon={<Zap size={18} />}
                  label="Practice"
                  value={selectedModule.practiceTotal}
                />

                <MiniStat
                  icon={<HelpCircle size={18} />}
                  label="Quiz"
                  value={selectedModule.quizTotal}
                />

                <MiniStat
                  icon={<GraduationCap size={18} />}
                  label="Progress"
                  value={`${moduleProgress.percentage}%`}
                />
              </div>
            </div>

            <div className="module-detail-panel">
              <div className="module-detail-tabs">
                <button
                  type="button"
                  className={
                    activeModuleTab === "lessons"
                      ? "module-detail-tab active"
                      : "module-detail-tab"
                  }
                  onClick={() => setActiveModuleTab("lessons")}
                >
                  <BookOpen size={17} />
                  Lessons
                </button>

                <button
                  type="button"
                  className={
                    activeModuleTab === "practice"
                      ? "module-detail-tab active"
                      : "module-detail-tab"
                  }
                  onClick={() => setActiveModuleTab("practice")}
                >
                  <Zap size={17} />
                  Practice
                </button>

                <button
                  type="button"
                  className={
                    activeModuleTab === "quiz"
                      ? "module-detail-tab active"
                      : "module-detail-tab"
                  }
                  onClick={() => setActiveModuleTab("quiz")}
                >
                  <CircleHelp size={17} />
                  Quiz
                </button>
              </div>

              {activeModuleTab === "lessons" && (
                <LessonsView
                  module={selectedModule}
                  lesson={lesson}
                  openedLesson={openedLesson}
                  setOpenedLesson={setOpenedLesson}
                  completedLessons={getCompletedLessonsForModule(
                    selectedModule.id
                  )}
                  markLessonCompleted={markLessonCompleted}
                />
              )}

              {activeModuleTab === "practice" && (
                <PracticeView
                  practice={practice}
                  practiceResults={practiceResults}
                  checkPractice={checkPractice}
                  clearPracticeResults={clearPracticeResults}
                  completedPractice={getCompletedPracticeForModule(
                    selectedModule.id
                  )}
                />
              )}

              {activeModuleTab === "quiz" && (
                <QuizView
                  quiz={quiz}
                  quizAnswers={quizAnswers}
                  setQuizAnswers={setQuizAnswers}
                  submitQuiz={submitQuiz}
                  quizResult={quizResult}
                  redoQuiz={redoQuiz}
                  quizStatus={quizStatus}
                />
              )}
            </div>
          </main>

          <OverallProgressCard
            title="Your Progress"
            subtitle={`${selectedModule.title} Module`}
            percentage={moduleProgress.percentage}
            lessons={`${moduleProgress.lessonsCompleted} / ${selectedModule.lessonsTotal}`}
            practice={`${moduleProgress.practiceCompleted} / ${selectedModule.practiceTotal}`}
            quizzes={`${moduleProgress.quizzesCompleted} / 1`}
            quizScore={`${moduleProgress.quizScore}%`}
            lessonPercent={moduleProgress.lessonPercent}
            practicePercent={moduleProgress.practicePercent}
            quizCompletionPercent={moduleProgress.quizCompletionPercent}
            quizScorePercent={moduleProgress.quizScorePercent}
            user={user}
            openAuthModal={openAuthModal}
          />
        </div>
      </section>
    );
  }

  return (
    <section className="education-v2 overview-page">
      {error && <div className="error">{error}</div>}

      <div className="education-v2-hero">
        <div className="education-badge-v2">✦ Interactive Learning</div>

        <h2>
          Choose a <span>Module</span>
        </h2>

        <p>
          Master each number theory topic through lessons, practice problems,
          and quizzes. Each module is separate, so you can start with any topic.
        </p>
      </div>

      {!user && <SaveProgressNote openAuthModal={openAuthModal} />}

      <div className="education-main-grid education-overview-grid">
        <main className="education-modules-area">
          <div className="module-list-vertical">
            {Object.values(MODULE_CONFIG).map((module) => {
              const progress = getModuleProgress(module.id);

              return (
                <button
                  type="button"
                  className="module-row-card"
                  key={module.id}
                  onClick={() => openModule(module.id)}
                >
                  <div className="module-row-icon">{module.icon}</div>

                  <div className="module-row-info">
                    <h3>{module.title}</h3>
                    <p>{module.description}</p>
                  </div>

                  <div className="module-row-stats">
                    <div className="module-stat-box">
                      <BookOpen size={19} />
                      <span>Lessons</span>
                      <strong>{module.lessonsTotal}</strong>
                    </div>

                    <div className="module-stat-box">
                      <Zap size={19} />
                      <span>Practice</span>
                      <strong>{module.practiceTotal}</strong>
                    </div>

                    <div className="module-stat-box">
                      <HelpCircle size={19} />
                      <span>Quiz</span>
                      <strong>{module.quizTotal}</strong>
                    </div>
                  </div>

                  <div
                    className="module-small-ring"
                    style={{
                      background: `conic-gradient(#8e5bff ${progress.percentage}%, #efe7f1 0)`,
                    }}
                  >
                    <span>{progress.percentage}%</span>
                  </div>

                  <ArrowRight size={20} className="module-row-arrow" />
                </button>
              );
            })}
          </div>
        </main>

        <OverallProgressCard
          title="Your Progress"
          subtitle="Overall completion"
          percentage={overallProgress.overall}
          lessons={`${overallProgress.lessonsCompleted} / ${overallProgress.totalLessons}`}
          practice={`${overallProgress.practiceCompleted} / ${overallProgress.totalPractice}`}
          quizzes={`${overallProgress.quizzesCompleted} / ${overallProgress.totalQuizzes}`}
          quizScore={`${overallProgress.averageQuizScore}%`}
          lessonPercent={overallProgress.lessonPercent}
          practicePercent={overallProgress.practicePercent}
          quizCompletionPercent={overallProgress.quizCompletionPercent}
          quizScorePercent={overallProgress.averageQuizScore}
          user={user}
          openAuthModal={openAuthModal}
        />
      </div>

      <div className="education-self-paced">
        <div className="bottom-note-icon">✦</div>
        <div>
          <strong>Learn at your own pace</strong>
          <p>
            Start with any module, review the lessons, practice problems, and
            test yourself with a quiz.
          </p>
        </div>
      </div>
    </section>
  );
}

function SaveProgressNote({ openAuthModal }) {
  return (
    <div className="save-progress-note">
      <div className="save-progress-icon">
        <Trophy size={20} />
      </div>

      <div>
        <strong>Want to save your progress?</strong>
        <p>
          Sign in or create an account so your completed lessons, practice
          problems, and quiz scores stay saved.
        </p>
      </div>

      <div className="save-progress-actions">
        <button type="button" onClick={() => openAuthModal("signin")}>
          Sign In
        </button>

        <button type="button" onClick={() => openAuthModal("create")}>
          Create Account
        </button>
      </div>
    </div>
  );
}

function MiniStat({ icon, label, value }) {
  return (
    <div className="mini-stat">
      <div>{icon}</div>
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function OverallProgressCard({
  title,
  subtitle,
  percentage,
  lessons,
  practice,
  quizzes,
  quizScore,
  lessonPercent = 0,
  practicePercent = 0,
  quizCompletionPercent = 0,
  quizScorePercent = 0,
  user,
  openAuthModal,
}) {
  return (
    <aside className="overall-progress-square">
      <div className="progress-title-row">
        <div className="progress-title-icon">
          <BarChart3 size={19} />
        </div>

        <div>
          <h3>{title}</h3>
          <p>{subtitle}</p>
        </div>
      </div>

      <div
        className="progress-donut"
        style={{
          background: `conic-gradient(#8e5bff ${percentage}%, #efe7f1 0)`,
        }}
      >
        <div>
          <strong>{percentage}%</strong>
          <span>Overall</span>
        </div>
      </div>

      <div className="progress-lines">
        <ProgressLine
          icon={<BookOpen size={18} />}
          label="Lessons Completed"
          value={lessons}
          percent={lessonPercent}
        />

        <ProgressLine
          icon={<Zap size={18} />}
          label="Practice Completed"
          value={practice}
          percent={practicePercent}
        />

        <ProgressLine
          icon={<HelpCircle size={18} />}
          label="Quizzes Completed"
          value={quizzes}
          percent={quizCompletionPercent}
        />

        <ProgressLine
          icon={<Trophy size={18} />}
          label="Quiz Score"
          value={quizScore}
          percent={quizScorePercent}
        />
      </div>

      {!user && (
        <button
          type="button"
          className="progress-primary-button"
          onClick={() => openAuthModal("signin")}
        >
          Sign in to save progress
          <ArrowRight size={17} />
        </button>
      )}
    </aside>
  );
}

function ProgressLine({ icon, label, value, percent = 0 }) {
  return (
    <div className="progress-line">
      <div className="progress-line-icon">{icon}</div>

      <div>
        <span>{label}</span>
        <div className="progress-line-track">
          <div
            className="progress-line-fill"
            style={{ width: `${Math.min(100, Math.max(0, percent))}%` }}
          />
        </div>
      </div>

      <strong>{value}</strong>
    </div>
  );
}

function LessonsView({
  module,
  lesson,
  openedLesson,
  setOpenedLesson,
  completedLessons,
  markLessonCompleted,
}) {
  const lessons =
    lesson?.lessons && lesson.lessons.length > 0
      ? lesson.lessons
      : module.lessons.map((title, index) => ({
          id: `${module.id}_lesson_${index + 1}`,
          title,
          summary: "Understand the idea with explanations and examples.",
          example: "",
          steps: [],
        }));

  return (
    <div className="module-section-content">
      <div className="module-section-header">
        <div>
          <h3>Lessons</h3>
          <p>Learn the core concepts step by step.</p>
        </div>

        <span>{lessons.length} Lessons</span>
      </div>

      <div className="lesson-list-v2">
        {lessons.map((lessonItem, index) => {
          const isCompleted = Boolean(completedLessons[lessonItem.id]);

          return (
            <div className="lesson-row-v2 lesson-row-clean" key={lessonItem.id}>
              <div className="lesson-number">{index + 1}</div>

              <div className="lesson-row-info">
                <h4>{lessonItem.title}</h4>
                <p>
                  Open the lesson to view the explanation, example, and steps.
                </p>
              </div>

              <span className="lesson-time">{10 + index * 2} min</span>

              <span
                className={
                  isCompleted ? "status-pill completed" : "status-pill"
                }
              >
                {isCompleted ? "Completed" : "Not started"}
              </span>

              <button
                type="button"
                className={isCompleted ? "review-button" : "start-button"}
                onClick={() => setOpenedLesson(lessonItem)}
              >
                {isCompleted ? "Review" : "Start Lesson"}
              </button>
            </div>
          );
        })}
      </div>

      <div className="education-self-paced compact">
        <div className="bottom-note-icon">✦</div>

        <div>
          <strong>Complete this module</strong>
          <p>
            Finish the lessons, practice problems, and quiz to master{" "}
            {module.title}.
          </p>
        </div>
      </div>

      {openedLesson && (
        <div
          className="lesson-modal-backdrop"
          onClick={() => setOpenedLesson(null)}
        >
          <div
            className="lesson-modal"
            onClick={(event) => event.stopPropagation()}
          >
            <button
              type="button"
              className="lesson-modal-close"
              onClick={() => setOpenedLesson(null)}
            >
              ×
            </button>

            <div className="lesson-modal-header">
              <div className="lesson-modal-icon">
                <BookOpen size={26} />
              </div>

              <div>
                <span>Lesson</span>
                <h2>{openedLesson.title}</h2>
              </div>
            </div>

            <div className="lesson-modal-section">
              <h3>Explanation</h3>
              <p>{openedLesson.summary}</p>
            </div>

            {openedLesson.example && (
              <div className="lesson-modal-section lesson-example-box">
                <h3>Example</h3>
                <p>{openedLesson.example}</p>
              </div>
            )}

            {openedLesson.steps && openedLesson.steps.length > 0 && (
              <div className="lesson-modal-section">
                <h3>Steps</h3>
                <ol>
                  {openedLesson.steps.map((step, index) => (
                    <li key={index}>{step}</li>
                  ))}
                </ol>
              </div>
            )}

            <div className="lesson-modal-actions">
              <button
                type="button"
                className="lesson-modal-secondary"
                onClick={() => setOpenedLesson(null)}
              >
                Close
              </button>

              <button
                type="button"
                className="lesson-modal-primary"
                onClick={() => markLessonCompleted(module.id, openedLesson.id)}
              >
                Mark as Done
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function PracticeView({
  practice,
  practiceResults,
  checkPractice,
  clearPracticeResults,
  completedPractice,
}) {
  const [activeLevel, setActiveLevel] = useState("easy");
  const [currentStepByExercise, setCurrentStepByExercise] = useState({});
  const [stepAnswers, setStepAnswers] = useState({});
  const [revealedAnswers, setRevealedAnswers] = useState({});

  const filteredPractice = practice.filter((item) => item.level === activeLevel);

  function getStepKey(exerciseId, stepId) {
    return `${exerciseId}:${stepId}`;
  }

  function getAnswer(exerciseId, stepId) {
    return stepAnswers[getStepKey(exerciseId, stepId)] || "";
  }

  function setAnswer(exerciseId, stepId, value) {
    const key = getStepKey(exerciseId, stepId);

    setStepAnswers((previous) => ({
      ...previous,
      [key]: value,
    }));
  }

  async function handleCheckStep(exercise, step, stepIndex) {
    const answer = getAnswer(exercise.id, step.id);
    const result = await checkPractice(exercise.id, step.id, answer);

    if (!result) {
      return;
    }

    if (result.is_correct) {
      const nextStepIndex = stepIndex + 1;

      setCurrentStepByExercise((previous) => ({
        ...previous,
        [exercise.id]: Math.max(previous[exercise.id] || 0, nextStepIndex),
      }));
    }
  }

  function revealAnswer(exerciseId, stepId) {
    const key = getStepKey(exerciseId, stepId);

    setRevealedAnswers((previous) => ({
      ...previous,
      [key]: true,
    }));
  }

  function redoExercise(exerciseId) {
    setCurrentStepByExercise((previous) => ({
      ...previous,
      [exerciseId]: 0,
    }));

    setStepAnswers((previous) => {
      const next = { ...previous };

      Object.keys(next).forEach((key) => {
        if (key.startsWith(`${exerciseId}:`)) {
          delete next[key];
        }
      });

      return next;
    });

    setRevealedAnswers((previous) => {
      const next = { ...previous };

      Object.keys(next).forEach((key) => {
        if (key.startsWith(`${exerciseId}:`)) {
          delete next[key];
        }
      });

      return next;
    });

    clearPracticeResults(exerciseId);
  }

  return (
    <div className="module-section-content">
      <div className="module-section-header">
        <div>
          <h3>Practice</h3>
          <p>Choose a level and solve step-by-step problems.</p>
        </div>

        <span>{filteredPractice.length} Problems</span>
      </div>

      <div className="difficulty-row">
        <button
          type="button"
          className={
            activeLevel === "easy" ? "difficulty-chip active" : "difficulty-chip"
          }
          onClick={() => setActiveLevel("easy")}
        >
          Easy
        </button>

        <button
          type="button"
          className={
            activeLevel === "medium"
              ? "difficulty-chip active"
              : "difficulty-chip"
          }
          onClick={() => setActiveLevel("medium")}
        >
          Medium
        </button>

        <button
          type="button"
          className={
            activeLevel === "hard" ? "difficulty-chip active" : "difficulty-chip"
          }
          onClick={() => setActiveLevel("hard")}
        >
          Hard
        </button>
      </div>

      {filteredPractice.map((exercise, exerciseIndex) => {
        const exerciseCompleted = Boolean(completedPractice?.[exercise.id]);
        const currentStepIndex = currentStepByExercise[exercise.id] || 0;
        const visibleSteps = exercise.steps.slice(0, currentStepIndex + 1);

        return (
          <div className="practice-card-v2" key={exercise.id}>
            <div className="practice-card-header">
              <span>Problem {exerciseIndex + 1}</span>
              <span>{exercise.level}</span>
            </div>

            <h4>{exercise.title}</h4>
            <p className="practice-question-text">{exercise.question}</p>

            {exerciseCompleted && (
              <div className="practice-complete-box">
                <CheckCircle size={18} />
                <strong>Already completed</strong>

                <button
                  type="button"
                  className="redo-button"
                  onClick={() => redoExercise(exercise.id)}
                >
                  Redo it
                </button>
              </div>
            )}

            <div className="practice-steps-list">
              {visibleSteps.map((step, stepIndex) => {
                const key = getStepKey(exercise.id, step.id);
                const result = practiceResults[key];
                const isRevealed = revealedAnswers[key];
                const isCorrect = result?.is_correct;

                return (
                  <div className="practice-step-card" key={step.id}>
                    <h5>{step.prompt}</h5>

                    {step.hint && (
                      <div className="hint-box">
                        <Lightbulb size={15} />
                        <span>{step.hint}</span>
                      </div>
                    )}

                    {step.type === "choice" ? (
                      <div className="step-choice-grid">
                        {step.options.map((option) => (
                          <button
                            type="button"
                            key={option.id}
                            className={
                              getAnswer(exercise.id, step.id) === option.id
                                ? "step-choice active"
                                : "step-choice"
                            }
                            onClick={() =>
                              setAnswer(exercise.id, step.id, option.id)
                            }
                            disabled={isCorrect}
                          >
                            <strong>{option.id.toUpperCase()}</strong>
                            <span>{option.text}</span>
                          </button>
                        ))}
                      </div>
                    ) : (
                      <input
                        placeholder="Enter your answer"
                        value={getAnswer(exercise.id, step.id)}
                        onChange={(event) =>
                          setAnswer(exercise.id, step.id, event.target.value)
                        }
                        disabled={isCorrect}
                      />
                    )}

                    <div className="step-action-row">
                      {!isCorrect && (
                        <button
                          type="button"
                          className="step-check-button"
                          onClick={() =>
                            handleCheckStep(exercise, step, stepIndex)
                          }
                        >
                          Check Step
                        </button>
                      )}

                      {result && !result.is_correct && (
                        <button
                          type="button"
                          className="step-reveal-button"
                          onClick={() => revealAnswer(exercise.id, step.id)}
                        >
                          Show Answer
                        </button>
                      )}

                      {isCorrect && (
                        <span className="step-correct-pill">Correct</span>
                      )}
                    </div>

                    {result && (
                      <div
                        className={
                          result.is_correct
                            ? "education-feedback correct"
                            : "education-feedback incorrect"
                        }
                      >
                        <div className="feedback-title">
                          {result.is_correct ? (
                            <CheckCircle size={18} />
                          ) : (
                            <XCircle size={18} />
                          )}

                          <strong>{result.message}</strong>
                        </div>

                        {result.is_correct && <p>{result.explanation}</p>}

                        {!result.is_correct && isRevealed && (
                          <>
                            <p>
                              <strong>Correct answer:</strong>{" "}
                              {result.correct_answer}
                            </p>
                            <p>{result.explanation}</p>
                          </>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            {currentStepIndex >= exercise.steps.length && (
              <div className="practice-complete-box">
                <CheckCircle size={18} />
                <strong>Problem completed!</strong>

                <button
                  type="button"
                  className="redo-button"
                  onClick={() => redoExercise(exercise.id)}
                >
                  Redo it
                </button>
              </div>
            )}
          </div>
        );
      })}

      {filteredPractice.length === 0 && (
        <div className="practice-card-v2">
          <h4>No problems for this level yet.</h4>
        </div>
      )}
    </div>
  );
}

function QuizView({
  quiz,
  quizAnswers,
  setQuizAnswers,
  submitQuiz,
  quizResult,
  redoQuiz,
  quizStatus,
}) {
  function setQuizAnswer(questionId, value) {
    setQuizAnswers((previous) => ({
      ...previous,
      [questionId]: value,
    }));
  }

  const completedFromSavedProgress = Boolean(quizStatus?.completed);
  const hasCurrentResult = Boolean(quizResult);

  return (
    <div className="module-section-content">
      <div className="module-section-header">
        <div>
          <h3>Quiz</h3>
          <p>Test your understanding of this module.</p>
        </div>

        <span>{quiz.length} Questions</span>
      </div>

      {completedFromSavedProgress && !hasCurrentResult && (
        <div className="quiz-completed-banner">
          <CheckCircle size={18} />
          <div>
            <strong>Quiz already completed</strong>
            <p>
              Best saved score: {quizStatus.bestScore}% across{" "}
              {quizStatus.attempts} attempt
              {quizStatus.attempts === 1 ? "" : "s"}.
            </p>
          </div>

          <button type="button" className="redo-button" onClick={redoQuiz}>
            Redo it
          </button>
        </div>
      )}

      {quiz.map((question, index) => {
        const resultForQuestion = quizResult?.results?.find(
          (result) => result.question_id === question.id
        );

        return (
          <div className="quiz-card-v2" key={question.id}>
            <div className="practice-card-header">
              <span>Question {index + 1}</span>

              <span>
                {resultForQuestion
                  ? resultForQuestion.is_correct
                    ? "Completed"
                    : "Reviewed"
                  : question.type === "input"
                  ? "Input"
                  : "MCQ"}
              </span>
            </div>

            <h4>{question.question}</h4>

            {question.type === "input" ? (
              <input
                placeholder="Enter your answer"
                value={quizAnswers[question.id] || ""}
                onChange={(event) =>
                  setQuizAnswer(question.id, event.target.value)
                }
                disabled={hasCurrentResult}
              />
            ) : (
              <div className="quiz-options">
                {question.options.map((option) => (
                  <label className="quiz-option" key={option.id}>
                    <input
                      type="radio"
                      name={question.id}
                      checked={quizAnswers[question.id] === option.id}
                      onChange={() => setQuizAnswer(question.id, option.id)}
                      disabled={hasCurrentResult}
                    />
                    <span>{option.text}</span>
                  </label>
                ))}
              </div>
            )}

            {resultForQuestion && (
              <div
                className={
                  resultForQuestion.is_correct
                    ? "education-feedback correct"
                    : "education-feedback incorrect"
                }
              >
                <div className="feedback-title">
                  {resultForQuestion.is_correct ? (
                    <CheckCircle size={18} />
                  ) : (
                    <XCircle size={18} />
                  )}

                  <strong>
                    {resultForQuestion.is_correct ? "Correct" : "Incorrect"}
                  </strong>
                </div>

                <p>{resultForQuestion.explanation}</p>
              </div>
            )}
          </div>
        );
      })}

      <div className="button-row quiz-action-row">
        {!hasCurrentResult && (
          <button type="button" onClick={submitQuiz}>
            Submit Quiz
          </button>
        )}

        {(hasCurrentResult || completedFromSavedProgress) && (
          <button type="button" className="secondary" onClick={redoQuiz}>
            Redo it
          </button>
        )}
      </div>

      {quizResult && (
        <div className="quiz-result-box">
          <h3>
            Score: {quizResult.score}/{quizResult.total} —{" "}
            {quizResult.percentage}%
          </h3>

          {quizResult.results.map((result, index) => (
            <div className="quiz-explanation" key={result.question_id}>
              <p>
                <strong>Question {index + 1}:</strong>{" "}
                {result.is_correct ? "Correct" : "Incorrect"}
              </p>

              {result.type === "mcq" ? (
                <>
                  <p>
                    <strong>Your answer:</strong>{" "}
                    {result.selected_option_id || "No answer"}
                  </p>
                  <p>
                    <strong>Correct answer:</strong>{" "}
                    {result.correct_option_id}
                  </p>
                </>
              ) : (
                <>
                  <p>
                    <strong>Your answer:</strong>{" "}
                    {result.user_answer || "No answer"}
                  </p>
                  <p>
                    <strong>Correct answer:</strong> {result.correct_answer}
                  </p>
                </>
              )}

              <p>{result.explanation}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default EducationTab;