import { useState } from "react";
import "./App.css";

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
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ n: Number(number) })
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
    if (result?.phi !== undefined) {
      await navigator.clipboard.writeText(String(result.phi));
      setCopied(true);
    }
  };

  return (
    <div className="tool-content">

      <main className="module-container">
        <div className="card">
          <input
            type="number"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            placeholder="Enter a number"
          />

          <div className="button-row">
            <button onClick={handleTotient}>Compute Totient</button>
            <button
              className="secondary"
              onClick={() => {
                setNumber("");
                setResult(null);
                setError("");
                setCopied(false);
              }}
            >
              Clear
            </button>
          </div>

          {error && <p className="error">{error}</p>}

          {result && (
            <div className="result-box">
              <h2>Result</h2>
              <p><strong>Input:</strong> {result.input}</p>
              <p><strong>φ(n):</strong> {result.phi}</p>
              <p><strong>Formula:</strong> {result.formula}</p>

              <button onClick={handleCopy}>
                {copied ? "Copied!" : "Copy Result"}
              </button>

              <h3>Prime Factors Used</h3>
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

export default TotientTab;