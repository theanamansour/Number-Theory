import { useState } from "react";
import "./App.css";
import TotientTab from "./TotientTab";
import PrimeFactorizationTab from "./PrimeFactorizationTab";
import MillerRabinTab from "./MillerRabinTab";
import FastExponentiationTab from "./FastExpTab";
import CRTTab from "./CRTTab";

function App() {
  const [activeTab, setActiveTab] = useState("totient");

  return (
    <div className="app">
      <header className="hero">
        <h1>Number Theory Toolkit</h1>
      </header>

      <nav className="tabs">
        <button
          className={activeTab === "factorization" ? "tab active" : "tab"}
          onClick={() => setActiveTab("factorization")}
        >
          Prime Factorization
        </button>

        <button
          className={activeTab === "totient" ? "tab active" : "tab"}
          onClick={() => setActiveTab("totient")}
        >
          Euler Totient Function
        </button>

        <button
          className={activeTab === "miller-rabin" ? "tab active" : "tab"}
          onClick={() => setActiveTab("miller-rabin")}
        >
          Miller-Rabin Test
        </button>

        <button
          className={activeTab === "fast-exp" ? "tab active" : "tab"}
          onClick={() => setActiveTab("fast-exp")}
        >
          Fast Exponentiation
        </button>

        <button
          className={activeTab === "crt" ? "tab active" : "tab"}
          onClick={() => setActiveTab("crt")}
        >
          Chinese Remainder Theorem
        </button>
      </nav>

      <main className="module-container">
        {activeTab === "factorization" && <PrimeFactorizationTab />}

        {activeTab === "totient" && <TotientTab />}

        {activeTab === "miller-rabin" && <MillerRabinTab />}

        {activeTab === "fast-exp" && <FastExponentiationTab />}

        {activeTab === "crt" && <CRTTab />}
        
      </main>
    </div>
  );
}

export default App;