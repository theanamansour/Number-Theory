import { useState } from "react";
import "./App.css";
import {
  Diamond,
  Lightbulb,
  Rocket,
  RotateCcw,
  Star,
  Info,
} from "lucide-react";

function getAuthHeaders() {
  const token = localStorage.getItem("token");

  return token
    ? { Authorization: `Bearer ${token}` }
    : {};
}

function MillerRabinTab() {
  const [number, setNumber] = useState("");
  const [base, setBase] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const handleMillerRabin = async () => {
    setError("");
    setResult(null);
    setCopied(false);

    if (!number || isNaN(number) || Number(number) < 3 || Number(number) % 2 === 0) {
      setError("Please enter an odd integer greater than or equal to 3.");
      return;
    }

    if (!base || isNaN(base)) {
      setError("Please enter a valid base a.");
      return;
    }

    const nValue = Number(number);
    const aValue = Number(base);

    if (aValue <= 1 || aValue >= nValue - 1) {
      setError("Base a must satisfy 1 < a < n - 1.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/millerrabin/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...getAuthHeaders(),
        },
        body: JSON.stringify({
          n: nValue,
          a: aValue,
        }),
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
    if (result) {
      const text = `Input: ${result.input}
Base: ${result.base}
Decomposition: ${result.decomposition}
Result: ${result.result}`;
      await navigator.clipboard.writeText(text);
      setCopied(true);
    }
  };

  const handleClear = () => {
    setNumber("");
    setBase("");
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
                  <Diamond size={30} strokeWidth={2.2} />
                </div>
                <div>
                  <h3>Miller–Rabin</h3>
                  <p>Test whether an odd integer is probably prime using a chosen base.</p>
                </div>
              </div>

              <label>Odd integer n</label>
              <input
                type="number"
                value={number}
                onChange={(e) => setNumber(e.target.value)}
                placeholder="e.g. 91"
              />

              <label>Base a</label>
              <input
                type="number"
                value={base}
                onChange={(e) => setBase(e.target.value)}
                placeholder="e.g. 3"
              />

              <div className="input-tip">
                <Lightbulb size={14} strokeWidth={1.8} />
                <span>Tip: Use an odd n ≥ 3 and a base where 1 &lt; a &lt; n - 1.</span>
              </div>

              <div className="button-row">
                <button onClick={handleMillerRabin}>
                  <Rocket size={16} strokeWidth={2} />
                  Run Test
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
                <button
                  className="example-chip"
                  onClick={() => {
                    setNumber("91");
                    setBase("3");
                  }}
                >
                  91, 3
                </button>
                <button
                  className="example-chip"
                  onClick={() => {
                    setNumber("221");
                    setBase("5");
                  }}
                >
                  221, 5
                </button>
                <button
                  className="example-chip"
                  onClick={() => {
                    setNumber("561");
                    setBase("2");
                  }}
                >
                  561, 2
                </button>
              </div>

              <div className="info-box">
                <div className="info-title">
                  <div className="info-icon">
                    <Info size={14} strokeWidth={2.2} />
                  </div>
                  <h4>What is Miller–Rabin?</h4>
                </div>

                <p>
                  Miller–Rabin is a probabilistic primality test that checks
                  whether a number is likely prime or definitely composite.
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
                  <span className="summary-label">Base</span>
                  <span className="summary-value">{result.base}</span>
                </div>

                <div className="summary-pill">
                  <span className="summary-label">Result</span>
                  <span className="summary-value">{result.result}</span>
                </div>

                <div className="summary-pill">
                  <span className="summary-label">Decomposition</span>
                  <span className="summary-value">{result.decomposition}</span>
                </div>
              </div>

              <div className="button-row">
                <button onClick={handleCopy}>
                  {copied ? "Copied!" : "Copy Result"}
                </button>
              </div>

              <div className="section-card">
                <h3>Test Sequence</h3>
                <ul>
                  {result.sequence.map((item, index) => (
                    <li key={index}>
                      {item.expression} = {item.value}
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

export default MillerRabinTab;