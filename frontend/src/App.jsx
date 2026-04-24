import { useState } from "react";
import "./App.css";
import TotientTab from "./TotientTab";
import PrimeFactorizationTab from "./PrimeFactorizationTab";
import MillerRabinTab from "./MillerRabinTab";
import FastExponentiationTab from "./FastExpTab";
import CRTTab from "./CRTTab";
import { Shield, Zap, Hash, Lightbulb, Rocket, RotateCcw, Star, Info, BookOpen, Sparkles } from "lucide-react";
import heroImage from "./assets/hero.png";

function App() {
  const [activeTab, setActiveTab] = useState("factorization");

  const tabs = [
    { key: "factorization", label: "Prime Factorization", icon: "⌘" },
    { key: "totient", label: "Euler Totient", icon: "φ" },
    { key: "miller-rabin", label: "Miller–Rabin", icon: "⟐" },
    { key: "fast-exp", label: "Fast Exponentiation", icon: <Zap size={16} strokeWidth={1.8} /> },
    { key: "crt", label: "CRT Solver", icon: "⊞" },
  ];

  return (
    <div className="app">
      <div className="hero-shell">
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
                  <Shield size={18} strokeWidth={1.5} />
                </div>
                <div>
                  <strong>Accurate</strong>
                  <span>Reliable results</span>
                </div>
              </div>

              <div className="feature-card">
                <div className="feature-icon">
                  <Zap size={18} strokeWidth={1.5} />
                </div>
                <div>
                  <strong>Fast</strong>
                  <span>Optimized algorithms</span>
                </div>
              </div>

              <div className="feature-card">
                <div className="feature-icon">
                  <BookOpen size={18} strokeWidth={1.5} />
                </div>
                <div>
                  <strong>Educational</strong>
                  <span>Step-by-step insights</span>
                </div>
              </div>

              <div className="feature-card">
                <div className="feature-icon">
                  <Sparkles size={18} strokeWidth={1.5} />
                </div>
                <div>
                  <strong>Beautiful</strong>
                  <span>Clean & intuitive UI</span>
                </div>
              </div>

            </div>
          </div>
          <div className="hero-right">
            <img src={heroImage} alt="Number theory illustration" className="hero-image" />
          </div>
        </header>

        <section className="workspace-shell">
          <nav className="workspace-tabs">
            {tabs.map((tab) => (
              <button
                key={tab.key}
                className={activeTab === tab.key ? "workspace-tab active" : "workspace-tab"}
                onClick={() => setActiveTab(tab.key)}
                type="button"
              >
                <span className="tab-icon">{tab.icon}</span>
                {tab.label}
              </button>
            ))}
          </nav>

          <div className="workspace-content">
            {activeTab === "factorization" && <PrimeFactorizationTab />}
            {activeTab === "totient" && <TotientTab />}
            {activeTab === "miller-rabin" && <MillerRabinTab />}
            {activeTab === "fast-exp" && <FastExponentiationTab />}
            {activeTab === "crt" && <CRTTab />}
          </div>
        </section>

        <div className="bottom-note">
          <div className="bottom-note-icon">✦</div>
          <p>
            All computations are performed using efficient algorithms with
            step-by-step explanations.
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;