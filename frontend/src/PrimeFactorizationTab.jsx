import { useState } from "react";
import { Hash, Lightbulb, Rocket, RotateCcw, Star, Info } from "lucide-react";
import "./App.css";

function getAuthHeaders() {
  const token = localStorage.getItem("token");

  return token
    ? { Authorization: `Bearer ${token}` }
    : {};
}

function PrimeFactorizationTab() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const handleFactorization = async () => {
    setError("");
    setResult(null);
    setCopied(false);

    if (!number || isNaN(number) || Number(number) <= 0) {
      setError("Please enter a valid positive integer.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/factorization/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...getAuthHeaders(),
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

  const handleCopy = async () => {
    if (result?.formatted) {
      await navigator.clipboard.writeText(result.formatted);
      setCopied(true);
    }
  };

  const handleClear = () => {
    setNumber("");
    setResult(null);
    setError("");
    setCopied(false);
  };

  return (
    <div className="tool-content">
      <main className="module-container">
        <div className="card">
          <div className="tool-grid">
            <div className="tool-left">
              <div className="tool-title">
                <div className="tool-icon">
                  <Hash size={32} strokeWidth={2.5} />
                </div>
                <div>
                  <h3>Prime Factorization</h3>
                  <p>Decompose a positive integer into its prime factors.</p>
                </div>
              </div>

              <label>Enter a positive integer</label>
              <input
                type="number"
                value={number}
                onChange={(e) => setNumber(e.target.value)}
                placeholder="e.g. 360"
              />
              <div className="input-tip">
                <Lightbulb size={14} strokeWidth={1.8} />
                <span>Tip: Enter any number greater than 1.</span>
              </div>

              <div className="button-row">
                <button onClick={handleFactorization}>
                  <Rocket size={16} strokeWidth={2} />
                  Compute
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
                <button className="example-chip" onClick={() => setNumber("84")}>
                  84
                </button>
                <button className="example-chip" onClick={() => setNumber("360")}>
                  360
                </button>
                <button className="example-chip" onClick={() => setNumber("945")}>
                  945
                </button>
                <button className="example-chip" onClick={() => setNumber("1024")}>
                  1024
                </button>
              </div>

              <div className="info-box">
                <div className="info-title">
                  <div className="info-icon">
                    <Info size={14} strokeWidth={2.2} />
                  </div>
                  <h4>What is Prime Factorization?</h4>
                  </div>

                <p>
                  Every integer n &gt; 1 can be expressed uniquely
                  <br />
                  as a product of prime powers.
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
                  <span className="summary-label">Factorization</span>
                  <span className="summary-value">{result.formatted}</span>
                </div>
              </div>

              <div className="button-row">
                <button onClick={handleCopy}>
                  {copied ? "Copied!" : "Copy Result"}
                </button>
              </div>

              <div className="section-card">
                <h3>Prime Factors</h3>
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

export default PrimeFactorizationTab;