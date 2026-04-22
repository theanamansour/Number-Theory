import { useState } from "react";
import "./App.css";

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
      const response = await fetch("http://127.0.0.1:8000/api/fastexp/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          a: Number(base),
          b: Number(exponent),
          n: Number(modulus)
        })
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
      <header className="tool-header">
        <h2>Fast Exponentiation</h2>
        <p>
          Enter a base, exponent, and modulus to compute a^b mod n using fast exponentiation.
        </p>
      </header>

      <main className="module-container">
        <div className="card">
          <input
            type="number"
            value={base}
            onChange={(e) => setBase(e.target.value)}
            placeholder="Enter base a"
          />

          <input
            type="number"
            value={exponent}
            onChange={(e) => setExponent(e.target.value)}
            placeholder="Enter exponent b"
          />

          <input
            type="number"
            value={modulus}
            onChange={(e) => setModulus(e.target.value)}
            placeholder="Enter modulus n"
          />

          <div className="button-row">
            <button onClick={handleFastExponentiation}>Compute</button>
            <button className="secondary" onClick={handleClear}>
              Clear
            </button>
          </div>

          {error && <p className="error">{error}</p>}

          {result && (
            <div className="result-box">
              <h2>Result</h2>
              <p><strong>Base:</strong> {result.base}</p>
              <p><strong>Exponent:</strong> {result.exponent}</p>
              <p><strong>Modulus:</strong> {result.modulus}</p>
              <p><strong>Value:</strong> {result.result}</p>

              <button onClick={handleCopy}>
                {copied ? "Copied!" : "Copy Result"}
              </button>

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

export default FastExponentiationTab;