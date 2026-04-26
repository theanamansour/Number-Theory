import { useEffect, useState } from "react";
import "./App.css";

import TotientTab from "./TotientTab";
import PrimeFactorizationTab from "./PrimeFactorizationTab";
import MillerRabinTab from "./MillerRabinTab";
import FastExponentiationTab from "./FastExpTab";
import CRTTab from "./CRTTab";
import EducationTab from "./EducationTab";
import ProfilePage from "./ProfilePage";

import {
  Shield,
  Zap,
  BookOpen,
  Sparkles,
  Home,
  LogOut,
} from "lucide-react";

import heroImage from "./assets/hero.png";

const AUTH_API = "http://127.0.0.1:8000/api/auth";

function App() {
  const [activePage, setActivePage] = useState("home");
  const [activeToolTab, setActiveToolTab] = useState("factorization");

  const [authMode, setAuthMode] = useState(null); // "signin" or "create"
  const [showPassword, setShowPassword] = useState(false);
  const [emailStatus, setEmailStatus] = useState(null);
  const [emailChecking, setEmailChecking] = useState(false);
  const [authEmail, setAuthEmail] = useState("");
  const [authUsername, setAuthUsername] = useState("");
  const [authPassword, setAuthPassword] = useState("");
  const [authError, setAuthError] = useState("");
  const [authLoading, setAuthLoading] = useState(false);

  const [user, setUser] = useState(null);

  const toolTabs = [
    { key: "factorization", label: "Prime Factorization", icon: "⌘" },
    { key: "totient", label: "Euler Totient", icon: "φ" },
    { key: "miller-rabin", label: "Miller–Rabin", icon: "⟐" },
    {
      key: "fast-exp",
      label: "Fast Exponentiation",
      icon: <Zap size={16} strokeWidth={1.8} />,
    },
    { key: "crt", label: "CRT Solver", icon: "⊞" },
  ];

  useEffect(() => {
    checkSavedLogin();
  }, []);

  async function checkSavedLogin() {
    const token = localStorage.getItem("token");

    if (!token) {
      return;
    }

    try {
      const response = await fetch(`${AUTH_API}/me`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (!response.ok) {
        localStorage.removeItem("token");
        setUser(null);
        return;
      }

      setUser(data.user);
    } catch {
      localStorage.removeItem("token");
      setUser(null);
    }
  }

  function openAuthModal(mode) {
    setAuthMode(mode);
    setAuthUsername("");
    setAuthEmail("");
    setAuthPassword("");
    setShowPassword(false);
    setAuthError("");
    setEmailStatus(null);
    setEmailChecking(false);
  }

  function closeAuthModal() {
    setAuthMode(null);
    setAuthUsername("");
    setAuthEmail("");
    setAuthPassword("");
    setAuthError("");
    setShowPassword(false);
    setAuthLoading(false);
    setEmailStatus(null);
    setEmailChecking(false);
  }

  function isValidEmailFormat(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  async function checkEmailAvailability() {
    const email = authEmail.trim();

    if (!email) {
      setEmailStatus(null);
      return;
    }

    if (!isValidEmailFormat(email)) {
      setEmailStatus({
        type: "error",
        message: "Please enter a valid email address.",
        available: false,
      });
      return;
    }

    try {
      setEmailChecking(true);

      const response = await fetch(`${AUTH_API}/email-status`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data?.detail || "Could not check email.");
      }

      if (authMode === "create") {
        setEmailStatus({
          type: data.available ? "success" : "error",
          message: data.available
            ? "Email is available."
            : "This email is already in use. Try signing in instead.",
          available: data.available,
        });
      } else {
        setEmailStatus({
          type: data.available ? "error" : "success",
          message: data.available
            ? "No account found with this email. Please create an account."
            : "Email found. You can sign in.",
          available: data.available,
        });
      }
    } catch (error) {
      setEmailStatus({
        type: "error",
        message: error.message,
        available: false,
      });
    } finally {
      setEmailChecking(false);
    }
  }

  async function submitAuth(event) {
    event.preventDefault();

    try {
      setAuthLoading(true);
      setAuthError("");

      if (!isValidEmailFormat(authEmail)) {
        throw new Error("Please enter a valid email address.");
      }

      if (authMode === "create" && emailStatus?.available === false) {
        throw new Error("This email is already in use. Please sign in instead.");
      }

      const endpoint = authMode === "create" ? "register" : "login";

      const response = await fetch(`${AUTH_API}/${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(
          authMode === "create"
            ? {
                username: authUsername,
                email: authEmail,
                password: authPassword,
              }
            : {
                email: authEmail,
                password: authPassword,
              }
        ),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data?.detail || "Authentication failed.");
      }

      if (authMode === "create") {
        const loginResponse = await fetch(`${AUTH_API}/login`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: authEmail,
            password: authPassword,
          }),
        });

        const loginData = await loginResponse.json();

        if (!loginResponse.ok) {
          throw new Error(
            loginData?.detail || "Account created, but login failed."
          );
        }

        localStorage.setItem("token", loginData.token);
        setUser(loginData.user);
      } else {
        localStorage.setItem("token", data.token);
        setUser(data.user);
      }

      closeAuthModal();
    } catch (error) {
      setAuthError(error.message);
    } finally {
      setAuthLoading(false);
    }
  }

  async function logout() {
    const token = localStorage.getItem("token");

    try {
      if (token) {
        await fetch(`${AUTH_API}/logout`, {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
      }
    } catch {
      // still log out locally even if the backend call fails
    }

    localStorage.removeItem("token");
    setUser(null);
  }

  return (
    <div className="app">
      <div className="hero-shell">
        <nav className="top-navbar">
          <button
            className="brand"
            type="button"
            onClick={() => setActivePage("home")}
          >
            <span className="brand-mark">φ8</span>
            <span>
              <strong>Number Theory</strong> Toolkit
            </span>
          </button>

          <div className="top-nav-links">
            <button
              type="button"
              className={
                activePage === "home" ? "top-nav-link active" : "top-nav-link"
              }
              onClick={() => setActivePage("home")}
            >
              <Home size={15} />
              Home
            </button>

            <button
              type="button"
              className={
                activePage === "education"
                  ? "top-nav-link active"
                  : "top-nav-link"
              }
              onClick={() => setActivePage("education")}
            >
              <BookOpen size={15} />
              Education
            </button>
          </div>

          <div className="auth-actions">
            {user ? (
              <>
                <button
                  type="button"
                  className={
                    activePage === "profile"
                      ? "user-pill user-pill-clickable active"
                      : "user-pill user-pill-clickable"
                  }
                  onClick={() => setActivePage("profile")}
                >
                  <span className="user-avatar">
                    {(user.username || user.email)?.charAt(0).toUpperCase()}
                  </span>
                  <span>{user.username || user.email}</span>
                </button>

                <button type="button" className="signin-button" onClick={logout}>
                  <LogOut size={15} />
                  Log Out
                </button>
              </>
            ) : (
              <>
                <button
                  type="button"
                  className="signin-button"
                  onClick={() => openAuthModal("signin")}
                >
                  Sign In
                </button>

                <button
                  type="button"
                  className="create-account-button"
                  onClick={() => openAuthModal("create")}
                >
                  Create Account
                </button>
              </>
            )}
          </div>
        </nav>

        {activePage === "home" && (
          <header className="hero">
            <div className="hero-left">
              <div className="eyebrow">interactive math toolkit</div>

              <h1>
                <span>Number Theory</span>
                <span className="hero-dark">Toolkit</span>
              </h1>

              <p>
                Explore fundamental algorithms and theorems of number theory with
                interactive tools and clear explanations.
              </p>

              <div className="feature-grid">
                <div className="feature-card">
                  <div className="feature-icon">
                    <Shield size={50} strokeWidth={1.5} />
                  </div>
                  <div>
                    <strong>Accurate</strong>
                    <span>Reliable results</span>
                  </div>
                </div>

                <div className="feature-card">
                  <div className="feature-icon">
                    <Zap size={50} strokeWidth={1.5} />
                  </div>
                  <div>
                    <strong>Fast</strong>
                    <span>Optimized algorithms</span>
                  </div>
                </div>

                <div className="feature-card">
                  <div className="feature-icon">
                    <BookOpen size={50} strokeWidth={1.5} />
                  </div>
                  <div>
                    <strong>Educational</strong>
                    <span>Step-by-step insights</span>
                  </div>
                </div>
              </div>
            </div>

            <div className="hero-right">
              <img
                src={heroImage}
                alt="Number theory illustration"
                className="hero-image"
              />
            </div>
          </header>
        )}

        {activePage === "home" && (
          <>
            <section className="workspace-shell">
              <nav className="workspace-tabs">
                {toolTabs.map((tab) => (
                  <button
                    key={tab.key}
                    className={
                      activeToolTab === tab.key
                        ? "workspace-tab active"
                        : "workspace-tab"
                    }
                    onClick={() => setActiveToolTab(tab.key)}
                    type="button"
                  >
                    <span className="tab-icon">{tab.icon}</span>
                    {tab.label}
                  </button>
                ))}
              </nav>

              <div className="workspace-content">
                {activeToolTab === "factorization" && <PrimeFactorizationTab />}
                {activeToolTab === "totient" && <TotientTab />}
                {activeToolTab === "miller-rabin" && <MillerRabinTab />}
                {activeToolTab === "fast-exp" && <FastExponentiationTab />}
                {activeToolTab === "crt" && <CRTTab />}
              </div>
            </section>

            <div className="bottom-note">
              <div className="bottom-note-icon">✦</div>
              <p>
                All computations are performed using efficient algorithms with
                step-by-step explanations.
              </p>
            </div>
          </>
        )}

        {activePage === "education" && (<EducationTab user={user} openAuthModal={openAuthModal} />)}
        {activePage === "profile" && (<ProfilePage user={user} openAuthModal={openAuthModal} setActivePage={setActivePage}
  />
)}
      </div>

      {authMode && (
        <div className="auth-modal-backdrop" onClick={closeAuthModal}>
          <div
            className="auth-modal"
            onClick={(event) => event.stopPropagation()}
          >
            <button
              type="button"
              className="auth-close"
              onClick={closeAuthModal}
            >
              ×
            </button>

            <div className="auth-modal-scroll">
              <div className="auth-modal-header">
                <div className="auth-modal-icon">
                  <BookOpen size={24} />
                </div>

                <h2>{authMode === "create" ? "Create Account" : "Sign In"}</h2>

                <p>
                  {authMode === "create"
                    ? "Create an account to save your history and education progress."
                    : "Sign in to save computations, track progress, and continue learning."}
                </p>
              </div>

              <form className="auth-form" onSubmit={submitAuth}>
                {authMode === "create" && (
                  <>
                    <label>Name</label>
                    <input
                      type="text"
                      value={authUsername}
                      onChange={(event) => setAuthUsername(event.target.value)}
                      placeholder="Enter your name"
                      required
                    />
                  </>
                )}

                <label>Email</label>
                <input
                  type="email"
                  value={authEmail}
                  onChange={(event) => {
                    setAuthEmail(event.target.value);
                    setEmailStatus(null);
                    setAuthError("");
                  }}
                  onBlur={checkEmailAvailability}
                  placeholder="you@example.com"
                  required
                />

                {emailChecking && (
                  <p className="email-status neutral">Checking email...</p>
                )}

                {emailStatus && !emailChecking && (
                  <p className={`email-status ${emailStatus.type}`}>
                    {emailStatus.message}
                  </p>
                )}

                <label>Password</label>
                <div className="password-input-wrapper">
                  <input
                    type={showPassword ? "text" : "password"}
                    value={authPassword}
                    onChange={(event) => setAuthPassword(event.target.value)}
                    placeholder="Enter your password"
                    required
                  />

                  <button
                    type="button"
                    className="show-password-button"
                    onClick={() => setShowPassword((previous) => !previous)}
                  >
                    {showPassword ? "Hide" : "Show"}
                  </button>
                </div>

                {authMode === "create" && (
                  <p className="password-note">
                    Password must be at least 8 characters and include
                    uppercase, lowercase, number, and special character.
                  </p>
                )}

                {authError && <div className="auth-error">{authError}</div>}

                <button
                  type="submit"
                  className="auth-submit"
                  disabled={authLoading}
                >
                  {authLoading
                    ? "Please wait..."
                    : authMode === "create"
                    ? "Create Account"
                    : "Sign In"}
                </button>
              </form>

              <div className="auth-switch">
                {authMode === "create" ? (
                  <p>
                    Already have an account?{" "}
                    <button
                      type="button"
                      onClick={() => openAuthModal("signin")}
                    >
                      Sign In
                    </button>
                  </p>
                ) : (
                  <p>
                    New here?{" "}
                    <button
                      type="button"
                      onClick={() => openAuthModal("create")}
                    >
                      Create Account
                    </button>
                  </p>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;