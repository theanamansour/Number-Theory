import { useState } from "react";
import "./App.css";

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
      <header className="tool-header">
        <h2>Prime Factorization</h2>
        <p>
          Enter a positive integer to compute its prime factorization, with
          factor list and step-by-step explanation.
        </p>
      </header>

      <main className="module-container">
        <div className="card">
          <input
            type="number"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            placeholder="Enter a number"
          />

          <div className="button-row">
            <button onClick={handleFactorization}>Compute Factorization</button>
            <button className="secondary" onClick={handleClear}>
              Clear
            </button>
          </div>

          {error && <p className="error">{error}</p>}

          {result && (
            <div className="result-box">
              <h2>Result</h2>
              <p><strong>Input:</strong> {result.input}</p>
              <p><strong>Prime Factorization:</strong> {result.formatted}</p>

              <button onClick={handleCopy}>
                {copied ? "Copied!" : "Copy Result"}
              </button>

              <h3>Prime Factors</h3>
              <ul>
                {result.factors.map((factor, index) => (
                  <li key={index}>
                    {factor.prime}^{factor.power}
                  </li>
                ))}
              </ul>

              <h3>Step-by-Step Explanation</h3>
              <ol>
                {result.steps.map((step, index) => (
                  <li key={index}>{step}</li>
                ))}
              </ol>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default PrimeFactorizationTab;