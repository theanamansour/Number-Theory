import { useState } from "react";
import "./App.css";
import {

  Zap,
  Lightbulb,
  Rocket,
  RotateCcw,
  Star,
  Info,
} from "lucide-react";
const API_BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

function getAuthHeaders() {
  const token = localStorage.getItem("token");

  return token
    ? { Authorization: `Bearer ${token}` }
    : {};
}

function FastExponentiationTab() {
  const [base, setBase] = useState("");
  const [exponent, setExponent] = useState("");
  const [modulus, setModulus] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const handleFastExponentiation = async () => {
    setError("");
    setResult(null);
    setCopied(false);

    if (base === "" || exponent === "" || modulus === "") {
      setError("Please fill in base, exponent, and modulus.");
      return;
    }

    if (isNaN(base) || isNaN(exponent) || isNaN(modulus)) {
      setError("Please enter valid integers.");
      return;
    }

    if (Number(exponent) < 0) {
      setError("Exponent must be non-negative.");
      return;
    }

    if (Number(modulus) <= 0) {
      setError("Modulus must be greater than 0.");
      return;
    }

    try {
      const response = await fetch(`${API_BASE}/api/fastexp/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...getAuthHeaders(),

        },
        body: JSON.stringify({
          a: Number(base),
          b: Number(exponent),
          n: Number(modulus),
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
      await navigator.clipboard.writeText(
        `${result.base}^${result.exponent} mod ${result.modulus} = ${result.result}`
      );
      setCopied(true);
    }
  };

  const handleClear = () => {
    setBase("");
    setExponent("");
    setModulus("");
    setResult(null);
    setError("");
    setCopied(false);
  };

  return (
    <div className="tool-content">
      <main className="module-container">
        <div className="card">
          <div className="tool-grid">
            {/* LEFT */}
            <div className="tool-left">
              <div className="tool-title">
                <div className="tool-icon">
                  <Zap size={30} strokeWidth={2.2} />
                </div>
                <div>
                  <h3>Fast Exponentiation</h3>
                  <p>Compute large powers modulo n efficiently.</p>
                </div>
              </div>

              <div className="input-grid">
                <div>
                  <label>Base a</label>
                  <input
                    type="number"
                    value={base}
                    onChange={(e) => setBase(e.target.value)}
                    placeholder="e.g. 5"
                  />
                </div>

                <div>
                  <label>Exponent b</label>
                  <input
                    type="number"
                    value={exponent}
                    onChange={(e) => setExponent(e.target.value)}
                    placeholder="e.g. 3"
                  />
                </div>

                <div className="full-width">
                  <label>Modulus n</label>
                  <input
                    type="number"
                    value={modulus}
                    onChange={(e) => setModulus(e.target.value)}
                    placeholder="e.g. 13"
                  />
                </div>
              </div>

              <div className="input-tip">
                <Lightbulb size={14} strokeWidth={1.8} />
                <span>
                  Tip: Use a non-negative exponent and a modulus greater than 0.
                </span>
              </div>

              <div className="button-row">
                <button onClick={handleFastExponentiation}>
                  <Rocket size={16} strokeWidth={2} />
                  Compute
                </button>

                <button className="secondary" onClick={handleClear}>
                  <RotateCcw size={16} strokeWidth={2} />
                  Clear
                </button>
              </div>
            </div>

            {/* RIGHT */}
            <div className="tool-right">
              <div className="examples-title">
                <Star size={14} strokeWidth={2} />
                <span>Try these examples</span>
              </div>

              {/* ✅ FIXED PART */}
              <div className="example-row fast-exp-row">
                <button
                  className="example-chip fast-exp-chip"
                  onClick={() => {
                    setBase("5");
                    setExponent("3");
                    setModulus("13");
                  }}
                >
                  5³ mod 13
                </button>

                <button
                  className="example-chip fast-exp-chip"
                  onClick={() => {
                    setBase("7");
                    setExponent("128");
                    setModulus("13");
                  }}
                >
                  7¹²⁸ mod 13
                </button>
              </div>

              <div className="info-box">
                <div className="info-title">
                  <div className="info-icon">
                    <Info size={14} strokeWidth={2.2} />
                  </div>
                  <h4>What is Fast Exponentiation?</h4>
                </div>

                <p>
                  Fast exponentiation computes powers efficiently by repeatedly
                  squaring instead of multiplying one step at a time.
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
                  <span className="summary-label">Base</span>
                  <span className="summary-value">{result.base}</span>
                </div>

                <div className="summary-pill">
                  <span className="summary-label">Exponent</span>
                  <span className="summary-value">{result.exponent}</span>
                </div>

                <div className="summary-pill">
                  <span className="summary-label">Modulus</span>
                  <span className="summary-value">{result.modulus}</span>
                </div>

                <div className="summary-pill">
                  <span className="summary-label">Value</span>
                  <span className="summary-value">{result.result}</span>
                </div>
              </div>

              <div className="button-row">
                <button onClick={handleCopy}>
                  {copied ? "Copied!" : "Copy Result"}
                </button>
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

export default FastExponentiationTab;
