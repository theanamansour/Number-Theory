import React, { useEffect, useMemo, useState } from "react";
import {
  User,
  Mail,
  CalendarDays,
  Calculator,
  BookOpen,
  Zap,
  Trophy,
  BarChart3,
  Clock,
  Eye,
  Search,
  Filter,
  Download,
  Trash2,
  GraduationCap,
  Hash,
  Grid2X2,
  Diamond,
} from "lucide-react";

const API_BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
const HISTORY_API = `${API_BASE}/api/history`;
const EDUCATION_API = `${API_BASE}/api/education`;

const MODULES = {
  factorization: {
    title: "Prime Factorization",
    icon: <Hash size={17} />,
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 1,
  },
  totient: {
    title: "Euler Totient",
    icon: "φ",
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 1,
  },
  fastexp: {
    title: "Fast Exponentiation",
    icon: <Zap size={17} />,
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 1,
  },
  millerrabin: {
    title: "Miller–Rabin",
    icon: <Diamond size={17} />,
    lessonsTotal: 5,
    practiceTotal: 6,
    quizTotal: 1,
  },
  crt: {
    title: "Chinese Remainder Theorem",
    icon: <Grid2X2 size={17} />,
    lessonsTotal: 4,
    practiceTotal: 6,
    quizTotal: 1,
  },
};

const OPERATION_LABELS = {
  prime_factorization: "Prime Factorization",
  euler_totient: "Euler Totient",
  fast_exponentiation: "Fast Exponentiation",
  miller_rabin: "Miller–Rabin",
  crt_residues: "CRT Residues",
  crt_recover: "CRT Recover",
};

function ProfilePage({ user, openAuthModal, setActivePage }) {
  const [history, setHistory] = useState([]);
  const [progressRows, setProgressRows] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [toolFilter, setToolFilter] = useState("all");
  const [error, setError] = useState("");

  useEffect(() => {
    loadProfileData();
  }, [user]);

  function getAuthHeaders() {
    const token = localStorage.getItem("token");

    if (!token) {
      return {};
    }

    return {
      Authorization: `Bearer ${token}`,
    };
  }

  async function fetchJSON(url) {
    const response = await fetch(url, {
      headers: {
        ...getAuthHeaders(),
      },
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(
        data?.detail ||
          data?.error?.message ||
          "Could not load profile data."
      );
    }

    return data;
  }

  async function loadProfileData() {
    try {
      setError("");

      if (!user) {
        setHistory([]);
        setProgressRows([]);
        return;
      }

      const [historyData, progressData] = await Promise.all([
        fetchJSON(`${HISTORY_API}/me`),
        fetchJSON(`${EDUCATION_API}/progress/me`),
      ]);

      setHistory(historyData.history || []);
      setProgressRows(progressData.progress || []);
    } catch (err) {
      setError(err.message);
    }
  }

  function getModuleProgress(moduleId) {
    const config = MODULES[moduleId];
    const rows = progressRows.filter((row) => row.topic_id === moduleId);

    const lessonsCompleted = new Set(
      rows
        .filter((row) => row.mode === "lesson" && row.is_correct)
        .map((row) => row.item_id)
    ).size;

    const practiceCompleted = new Set(
      rows
        .filter((row) => row.mode === "practice" && row.is_correct)
        .map((row) => row.item_id)
    ).size;

    const bestQuizScore = rows
      .filter((row) => row.mode === "quiz" && row.total)
      .reduce((best, row) => {
        const percentage = Math.round((row.score / row.total) * 100);
        return Math.max(best, percentage);
      }, 0);

    const lessonPercent = Math.round(
      (Math.min(lessonsCompleted, config.lessonsTotal) / config.lessonsTotal) *
        100
    );

    const practicePercent = Math.round(
      (Math.min(practiceCompleted, config.practiceTotal) /
        config.practiceTotal) *
        100
    );

    const percentage = Math.round(
      lessonPercent * 0.35 + practicePercent * 0.4 + bestQuizScore * 0.25
    );

    return {
      lessonsCompleted: Math.min(lessonsCompleted, config.lessonsTotal),
      practiceCompleted: Math.min(practiceCompleted, config.practiceTotal),
      quizCompleted: bestQuizScore > 0,
      bestQuizScore,
      percentage,
    };
  }

  const profileStats = useMemo(() => {
    const moduleIds = Object.keys(MODULES);

    const moduleProgress = moduleIds.map((moduleId) =>
      getModuleProgress(moduleId)
    );

    const modulesStarted = moduleProgress.filter(
      (module) => module.percentage > 0
    ).length;

    const modulesCompleted = moduleProgress.filter(
      (module) => module.percentage === 100
    ).length;

    const totalLessons = moduleProgress.reduce(
      (sum, module) => sum + module.lessonsCompleted,
      0
    );

    const totalPractice = moduleProgress.reduce(
      (sum, module) => sum + module.practiceCompleted,
      0
    );

    const quizzesAttempted = moduleProgress.filter(
      (module) => module.quizCompleted
    ).length;

    const averageQuizScore =
      moduleProgress.length > 0
        ? Math.round(
            moduleProgress.reduce(
              (sum, module) => sum + module.bestQuizScore,
              0
            ) / moduleProgress.length
          )
        : 0;

    const overallProgress =
      moduleProgress.length > 0
        ? Math.round(
            moduleProgress.reduce(
              (sum, module) => sum + module.percentage,
              0
            ) / moduleProgress.length
          )
        : 0;

    return {
      totalCalculations: history.length,
      modulesStarted,
      modulesCompleted,
      totalLessons,
      totalPractice,
      quizzesAttempted,
      averageQuizScore,
      overallProgress,
    };
  }, [history, progressRows]);

  const filteredHistory = history.filter((item) => {
    const label = OPERATION_LABELS[item.operation] || item.operation;

    const matchesSearch =
      label.toLowerCase().includes(searchTerm.toLowerCase()) ||
      JSON.stringify(item.input_data)
        .toLowerCase()
        .includes(searchTerm.toLowerCase()) ||
      JSON.stringify(item.result_data)
        .toLowerCase()
        .includes(searchTerm.toLowerCase());

    const matchesTool = toolFilter === "all" || item.operation === toolFilter;

    return matchesSearch && matchesTool;
  });

  const recentEducationActivity = progressRows.slice(0, 6);

  function formatDate(dateString) {
    if (!dateString) return "—";

    return new Date(dateString).toLocaleString([], {
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  }

  function formatInput(input) {
    if (!input) return "—";

    if (input.n !== undefined) return `n = ${input.n}`;
    if (input.a !== undefined && input.b !== undefined && input.n !== undefined) {
      return `${input.a}^${input.b} mod ${input.n}`;
    }
    if (input.A !== undefined && input.moduli) {
      return `A = ${input.A}, moduli = [${input.moduli.join(", ")}]`;
    }
    if (input.residues && input.moduli) {
      return `residues = [${input.residues.join(", ")}], moduli = [${input.moduli.join(", ")}]`;
    }

    return JSON.stringify(input);
  }

  function formatResult(result) {
    if (!result) return "—";

    if (result.formatted) return result.formatted;
    if (result.phi !== undefined) return `φ(${result.input}) = ${result.phi}`;
    if (result.result !== undefined) return String(result.result);
    if (result.A !== undefined) return `A = ${result.A}`;
    if (result.residues) return `[${result.residues.join(", ")}]`;

    return JSON.stringify(result);
  }

    function escapeCSV(value) {
    const text = value === null || value === undefined ? "" : String(value);
    const excelSafeText = `\t${text}`;
    return `"${excelSafeText.replace(/"/g, '""')}"`;
  }

  function cleanForCSV(value) {
    return String(value ?? "")
      .replaceAll("φ", "phi")
      .replaceAll("Φ", "Phi")
      .replaceAll("×", "x")
      .replaceAll("≡", "congruent to")
      .replaceAll("²", "^2")
      .replaceAll("³", "^3")
      .replaceAll("⁴", "^4")
      .replaceAll("⁵", "^5")
      .replaceAll("⁶", "^6")
      .replaceAll("⁷", "^7")
      .replaceAll("⁸", "^8")
      .replaceAll("⁹", "^9")
      .replaceAll("⁰", "^0")
      .replaceAll("–", "-")   // en dash
      .replaceAll("—", "-")   // em dash
      .replaceAll("−", "-")   // minus sign
      .replaceAll("¹", "^1");
  }

  function escapeCSV(value) {
    const text = cleanForCSV(value);
    const excelSafeText = `\t${text}`;
    return `"${excelSafeText.replace(/"/g, '""')}"`;
  }

  function handleExportHistory() {
    try {
      setError("");

      if (history.length === 0) {
        setError("No calculation history to export.");
        return;
      }

      const headers = ["Tool", "Input", "Result", "Date & Time"];

      const rows = history.map((item) => [
        OPERATION_LABELS[item.operation] || item.operation,
        formatInput(item.input_data),
        formatResult(item.result_data),
        item.created_at,
      ]);

      const csvContent = [
        "sep=,",
        headers.map(escapeCSV).join(","),
        ...rows.map((row) => row.map(escapeCSV).join(",")),
      ].join("\n");

      const blob = new Blob(["\uFEFF" + csvContent], {
        type: "text/csv;charset=utf-8;",
      });

      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");

      link.href = url;
      link.download = "number-theory-calculation-history.csv";

      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      URL.revokeObjectURL(url);
    } catch {
      setError("Could not export calculation history.");
    }
  }


  function handleExportHistory() {
    try {
      setError("");

      if (history.length === 0) {
        setError("No calculation history to export.");
        return;
      }

      const headers = ["Tool", "Input", "Result", "Date & Time"];

      const rows = history.map((item) => [
        OPERATION_LABELS[item.operation] || item.operation,
        formatInput(item.input_data),
        formatResult(item.result_data),
        item.created_at,
      ]);

      const csvContent = [
        headers.map(escapeCSV).join(","),
        ...rows.map((row) => row.map(escapeCSV).join(",")),
      ].join("\n");

      const blob = new Blob([csvContent], {
        type: "text/csv;charset=utf-8;",
      });

      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");

      link.href = url;
      link.download = "number-theory-calculation-history.csv";

      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      URL.revokeObjectURL(url);
    } catch {
      setError("Could not export calculation history.");
    }
  }

  async function handleClearHistory() {
    try {
      setError("");

      if (history.length === 0) {
        setError("No calculation history to clear.");
        return;
      }

      const confirmed = window.confirm(
        "Are you sure you want to clear your calculation history? This will not delete your account or education progress."
      );

      if (!confirmed) {
        return;
      }

      const response = await fetch(`${HISTORY_API}/me`, {
        method: "DELETE",
        headers: {
          ...getAuthHeaders(),
        },
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data?.detail ||
            data?.error?.message ||
            "Could not clear calculation history."
        );
      }

      setHistory([]);
      setSearchTerm("");
      setToolFilter("all");
    } catch (err) {
      setError(err.message);
    }
  }

  if (!user) {
    return (
      <section className="profile-page">
        <div className="profile-login-card">
          <div className="profile-login-icon">
            <User size={30} />
          </div>

          <h2>Sign in to view your profile</h2>
          <p>
            Your profile will show saved calculation history, completed lessons,
            practice progress, and quiz scores.
          </p>

          <div className="profile-login-actions">
            <button type="button" onClick={() => openAuthModal("signin")}>
              Sign In
            </button>
            <button type="button" onClick={() => openAuthModal("create")}>
              Create Account
            </button>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section className="profile-page">
      {error && <div className="error">{error}</div>}

      <div className="profile-header">
        <div>
          <div className="education-badge-v2">✦ Saved Dashboard</div>
          <h2>
            My <span>Profile</span>
          </h2>
          <p>Track your activity, saved progress, and learning history.</p>
        </div>

        <div className="profile-actions">
          <button
            type="button"
            className="profile-soft-button"
            onClick={handleExportHistory}
          >
            <Download size={16} />
            Export History
          </button>

          <button
            type="button"
            className="profile-danger-button"
            onClick={handleClearHistory}
          >
            <Trash2 size={16} />
            Clear History
          </button>
        </div>
      </div>

      <div className="profile-grid">
        <aside className="profile-left-column">
          <div className="profile-card profile-summary-card">
            <div className="profile-card-title">
              <User size={18} />
              <h3>Profile Summary</h3>
            </div>

            <div className="profile-user-block">
              <div className="profile-avatar">
                {(user.username || user.email)?.charAt(0).toUpperCase()}
              </div>

              <div>
                <h3>{user.username || "Student"}</h3>
                <p>
                  <Mail size={14} />
                  {user.email}
                </p>
                <p>
                  <CalendarDays size={14} />
                  Joined {formatDate(user.created_at)}
                </p>
              </div>
            </div>

            <div className="profile-mini-stats">
              <ProfileStat
                icon={<Calculator size={18} />}
                value={profileStats.totalCalculations}
                label="Total Calculations"
              />
              <ProfileStat
                icon={<BookOpen size={18} />}
                value={profileStats.modulesStarted}
                label="Modules Started"
              />
              <ProfileStat
                icon={<Trophy size={18} />}
                value={profileStats.modulesCompleted}
                label="Modules Completed"
              />
              <ProfileStat
                icon={<BarChart3 size={18} />}
                value={`${profileStats.averageQuizScore}%`}
                label="Avg Quiz Score"
              />
            </div>
          </div>

          <div className="profile-card profile-progress-card">
            <div className="profile-progress-top">
              <div>
                <h3>Education Progress</h3>
                <p>Overall progress across all modules</p>
              </div>

              <div
                className="profile-progress-donut"
                style={{
                  background: `conic-gradient(#8e5bff ${profileStats.overallProgress}%, #efe7f1 0)`,
                }}
              >
                <div>
                  <strong>{profileStats.overallProgress}%</strong>
                  <span>Overall</span>
                </div>
              </div>
            </div>

            <div className="profile-module-list">
              {Object.entries(MODULES).map(([moduleId, module]) => {
                const progress = getModuleProgress(moduleId);

                return (
                  <div className="profile-module-row" key={moduleId}>
                    <div className="profile-module-icon">{module.icon}</div>

                    <div>
                      <span>{module.title}</span>
                      <div className="profile-module-track">
                        <div
                          className="profile-module-fill"
                          style={{ width: `${progress.percentage}%` }}
                        />
                      </div>
                    </div>

                    <strong>{progress.percentage}%</strong>
                  </div>
                );
              })}
            </div>

            <button
              type="button"
              className="profile-wide-button"
              onClick={() => setActivePage("education")}
            >
              View Education Dashboard
              <ArrowMini />
            </button>
          </div>
        </aside>

        <main className="profile-main-column">
          <div className="profile-card profile-history-card">
            <div className="profile-section-header">
              <div>
                <h3>Calculation History</h3>
                <p>Your recent calculations using the toolkit.</p>
              </div>
            </div>

            <div className="profile-history-filters">
              <div className="profile-search">
                <Search size={16} />
                <input
                  placeholder="Search calculations..."
                  value={searchTerm}
                  onChange={(event) => setSearchTerm(event.target.value)}
                />
              </div>

              <div className="profile-filter">
                <Filter size={16} />
                <select
                  value={toolFilter}
                  onChange={(event) => setToolFilter(event.target.value)}
                >
                  <option value="all">All Tools</option>
                  {Object.entries(OPERATION_LABELS).map(([key, label]) => (
                    <option value={key} key={key}>
                      {label}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <div className="profile-history-table-wrap">
              <table className="profile-history-table">
                <thead>
                  <tr>
                    <th>Tool</th>
                    <th>Input</th>
                    <th>Result</th>
                    <th>Date & Time</th>
                    <th>Action</th>
                  </tr>
                </thead>

                <tbody>
                  {filteredHistory.map((item) => (
                    <tr key={item.id}>
                      <td>
                        <span className="history-tool-pill">
                          {OPERATION_LABELS[item.operation] || item.operation}
                        </span>
                      </td>
                      <td>{formatInput(item.input_data)}</td>
                      <td className="history-result">
                        {formatResult(item.result_data)}
                      </td>
                      <td>{formatDate(item.created_at)}</td>
                      <td>
                        <button type="button" className="history-view-button">
                          <Eye size={14} />
                          View
                        </button>
                      </td>
                    </tr>
                  ))}

                  {filteredHistory.length === 0 && (
                    <tr>
                      <td colSpan="5" className="profile-empty-row">
                        No saved calculations yet.
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>

          <div className="profile-card profile-education-card">
            <div className="profile-section-header">
              <div>
                <h3>Education Activity</h3>
                <p>Completed lessons, practice problems, and quiz attempts.</p>
              </div>
            </div>

            <div className="profile-education-stats">
              <ProfileStat
                icon={<BookOpen size={18} />}
                value={profileStats.totalLessons}
                label="Lessons Completed"
              />
              <ProfileStat
                icon={<Zap size={18} />}
                value={profileStats.totalPractice}
                label="Practice Solved"
              />
              <ProfileStat
                icon={<HelpIcon />}
                value={profileStats.quizzesAttempted}
                label="Quizzes Attempted"
              />
              <ProfileStat
                icon={<Trophy size={18} />}
                value={`${profileStats.averageQuizScore}%`}
                label="Best Avg Score"
              />
            </div>

            <div className="profile-activity-grid">
              <div className="profile-activity-panel">
                <h4>Recent Achievements</h4>

                <AchievementItem
                  icon={<Trophy size={16} />}
                  title="Learning Started"
                  text={`${profileStats.modulesStarted} module(s) started`}
                />
                <AchievementItem
                  icon={<BookOpen size={16} />}
                  title="Lesson Progress"
                  text={`${profileStats.totalLessons} lessons completed`}
                />
                <AchievementItem
                  icon={<Zap size={16} />}
                  title="Practice Solver"
                  text={`${profileStats.totalPractice} practice problems solved`}
                />
              </div>

              <div className="profile-activity-panel">
                <h4>Recent Education Activity</h4>

                {recentEducationActivity.map((row) => (
                  <div className="education-activity-item" key={row.id}>
                    <div className="activity-icon">
                      {row.mode === "lesson" ? (
                        <BookOpen size={15} />
                      ) : row.mode === "practice" ? (
                        <Zap size={15} />
                      ) : (
                        <Trophy size={15} />
                      )}
                    </div>

                    <div>
                      <strong>{formatEducationActivity(row)}</strong>
                      <span>{formatDate(row.created_at)}</span>
                    </div>
                  </div>
                ))}

                {recentEducationActivity.length === 0 && (
                  <p className="profile-muted-text">
                    No education activity yet.
                  </p>
                )}
              </div>
            </div>
          </div>
        </main>
      </div>
    </section>
  );
}

function formatEducationActivity(row) {
  const moduleName = MODULES[row.topic_id]?.title || row.topic_id;

  if (row.mode === "lesson") {
    return `Completed a lesson in ${moduleName}`;
  }

  if (row.mode === "practice") {
    return `Completed a practice problem in ${moduleName}`;
  }

  if (row.mode === "quiz") {
    return `Submitted quiz in ${moduleName}: ${row.score}/${row.total}`;
  }

  return `Worked on ${moduleName}`;
}

function ProfileStat({ icon, value, label }) {
  return (
    <div className="profile-stat">
      <div>{icon}</div>
      <strong>{value}</strong>
      <span>{label}</span>
    </div>
  );
}

function AchievementItem({ icon, title, text }) {
  return (
    <div className="achievement-item">
      <div>{icon}</div>
      <div>
        <strong>{title}</strong>
        <span>{text}</span>
      </div>
    </div>
  );
}

function HelpIcon() {
  return <Trophy size={18} />;
}

function ArrowMini() {
  return <span className="arrow-mini">›</span>;
}

export default ProfilePage;