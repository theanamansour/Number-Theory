import { useState } from "react";
import "./App.css";
import {
  CircleDot,
  Lightbulb,
  Rocket,
  RotateCcw,
  Star,
  Info,
} from "lucide-react";

function TotientTab() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const handleTotient = async () => {
    setError("");
    setResult(null);
    setCopied(false);

    if (!number || isNaN(number) || Number(number) <= 0) {
      setError("Please enter a valid positive integer.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/totient/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ n: Number(number) }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.detail || "Something went wrong.");
        return;
      }

      setResult(data);
    } catch {
      setError("Could not connect to backend.");
    }
  };

  const handleClear = () => {
    setNumber("");
    setResult(null);
    setError("");
    setCopied(false);
  };

  const handleCopy = async () => {
    if (result?.phi !== undefined) {
      await navigator.clipboard.writeText(String(result.phi));
      setCopied(true);
    }
  };

  return (
    <div className="tool-content">
      <main className="module-container">
        <div className="card">
          <div className="tool-grid">
            <div className="tool-left">
              <div className="tool-title">
                <div className="tool-icon">
                  <CircleDot size={30} strokeWidth={2.2} />
                </div>
                <div>
                  <h3>Euler Totient</h3>
                  <p>Count the integers up to n that are relatively prime to n.</p>
                </div>
              </div>

              <label>Enter a positive integer</label>
              <input
                type="number"
                value={number}
                onChange={(e) => setNumber(e.target.value)}
                placeholder="e.g. 36"
              />

              <div className="input-tip">
                <Lightbulb size={14} strokeWidth={1.8} />
                <span>Tip: Enter any number greater than 1.</span>
              </div>

              <div className="button-row">
                <button onClick={handleTotient}>
                  <Rocket size={16} strokeWidth={2} />
                  Compute Totient
                </button>

                <button className="secondary" onClick={handleClear}>
                  <RotateCcw size={16} strokeWidth={2} />
                  Clear
                </button>
              </div>
            </div>

            <div className="tool-right">
              <div className="examples-title">
                <Star size={14} strokeWidth={2} />
                <span>Try these examples</span>
              </div>

              <div className="example-row">
                <button className="example-chip" onClick={() => setNumber("9")}>
                  9
                </button>
                <button className="example-chip" onClick={() => setNumber("12")}>
                  12
                </button>
                <button className="example-chip" onClick={() => setNumber("36")}>
                  36
                </button>
                <button className="example-chip" onClick={() => setNumber("100")}>
                  100
                </button>
              </div>

              <div className="info-box">
                <div className="info-title">
                  <div className="info-icon">
                    <Info size={14} strokeWidth={2.2} />
                  </div>
                  <h4>What is Euler’s Totient?</h4>
                </div>

                <p>
                  φ(n) counts how many positive integers less than or equal to n
                  are relatively prime to n.
                </p>
              </div>
            </div>
          </div>

          {error && <p className="error">{error}</p>}

          {result && (
            <div className="result-box">
              <h2>Result</h2>

              <div className="result-summary">
                <div className="summary-pill">
                  <span className="summary-label">Input</span>
                  <span className="summary-value">{result.input}</span>
                </div>

                <div className="summary-pill">
                  <span className="summary-label">φ(n)</span>
                  <span className="summary-value">{result.phi}</span>
                </div>

                <div className="summary-pill">
                  <span className="summary-label">Formula</span>
                  <span className="summary-value">{result.formula}</span>
                </div>
              </div>

              <div className="button-row">
                <button onClick={handleCopy}>
                  {copied ? "Copied!" : "Copy Result"}
                </button>
              </div>

              <div className="section-card">
                <h3>Prime Factors Used</h3>
                <ul>
                  {result.factors.map((factor, index) => (
                    <li key={index}>
                      {factor.prime}^{factor.power}
                    </li>
                  ))}
                </ul>
              </div>

              <div className="section-card">
                <h3>Step-by-Step Explanation</h3>
                <ol>
                  {result.steps.map((step, index) => (
                    <li key={index}>{step}</li>
                  ))}
                </ol>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default TotientTab;