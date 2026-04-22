import { useState } from "react";
import "./App.css";

function CRTTab() {
  const [mode, setMode] = useState("A_to_residues");

  const [A, setA] = useState("");
  const [moduli, setModuli] = useState("");

  const [residues, setResidues] = useState("");

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const parseNumberList = (text) => {
    return text
      .split(",")
      .map((item) => item.trim())
      .filter((item) => item !== "")
      .map(Number);
  };

  const handleCRT = async () => {
    setError("");
    setResult(null);
    setCopied(false);

    const moduliList = parseNumberList(moduli);

    if (moduliList.length === 0 || moduliList.some(isNaN)) {
      setError("Please enter valid moduli separated by commas.");
      return;
    }

    try {
      let response;

      if (mode === "A_to_residues") {
        if (A === "" || isNaN(A)) {
          setError("Please enter a valid integer A.");
          return;
        }

        response = await fetch("http://127.0.0.1:8000/api/crt/residues", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            A: Number(A),
            moduli: moduliList
          })
        });
      } else {
        const residuesList = parseNumberList(residues);

        if (residuesList.length === 0 || residuesList.some(isNaN)) {
          setError("Please enter valid residues separated by commas.");
          return;
        }

        if (residuesList.length !== moduliList.length) {
          setError("Residues and moduli must have the same number of values.");
          return;
        }

        response = await fetch("http://127.0.0.1:8000/api/crt/recover", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            residues: residuesList,
            moduli: moduliList
          })
        });
      }

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
    if (!result) return;

    let text = "";

    if (mode === "A_to_residues") {
      text = `A = ${result.A}, moduli = [${result.moduli.join(", ")}], residues = [${result.residues.join(", ")}]`;
    } else {
      text = `Residues = [${result.residues.join(", ")}], moduli = [${result.moduli.join(", ")}], A = ${result.A} mod ${result.M}`;
    }

    await navigator.clipboard.writeText(text);
    setCopied(true);
  };

  const handleClear = () => {
    setA("");
    setModuli("");
    setResidues("");
    setResult(null);
    setError("");
    setCopied(false);
  };

  return (
    <div className="tool-content">
      <header className="tool-header">
        <h2>Chinese Remainder Theorem</h2>
        <p>
          Convert between A and its residues modulo pairwise relatively prime moduli.
        </p>
      </header>

      <main className="module-container">
        <div className="card">
          <div className="button-row">
            <button
              className={mode === "A_to_residues" ? "" : "secondary"}
              onClick={() => {
                setMode("A_to_residues");
                setResult(null);
                setError("");
                setCopied(false);
              }}
            >
              A → Residues
            </button>

            <button
              className={mode === "residues_to_A" ? "" : "secondary"}
              onClick={() => {
                setMode("residues_to_A");
                setResult(null);
                setError("");
                setCopied(false);
              }}
            >
              Residues → A
            </button>
          </div>

          {mode === "A_to_residues" && (
            <>
              <input
                type="number"
                value={A}
                onChange={(e) => setA(e.target.value)}
                placeholder="Enter A"
              />

              <input
                type="text"
                value={moduli}
                onChange={(e) => setModuli(e.target.value)}
                placeholder="Enter moduli separated by commas (e.g. a,b)"
              />
            </>
          )}

          {mode === "residues_to_A" && (
            <>
              <input
                type="text"
                value={residues}
                onChange={(e) => setResidues(e.target.value)}
                placeholder="Enter residues separated by commas (e.g. a,b)"
              />

              <input
                type="text"
                value={moduli}
                onChange={(e) => setModuli(e.target.value)}
                placeholder="Enter moduli separated by commas (e.g. a,b)"
              />
            </>
          )}

          <div className="button-row">
            <button onClick={handleCRT}>Compute CRT</button>
            <button className="secondary" onClick={handleClear}>
              Clear
            </button>
          </div>

          {error && <p className="error">{error}</p>}

          {result && (
            <div className="result-box">
              <h2>Result</h2>

              {mode === "A_to_residues" && (
                <>
                  <p><strong>A:</strong> {result.A}</p>
                  <p><strong>Moduli:</strong> {result.moduli.join(", ")}</p>
                  <p><strong>Residues:</strong> {result.residues.join(", ")}</p>
                </>
              )}

              {mode === "residues_to_A" && (
                <>
                  <p><strong>Residues:</strong> {result.residues.join(", ")}</p>
                  <p><strong>Moduli:</strong> {result.moduli.join(", ")}</p>
                  <p><strong>M:</strong> {result.M}</p>
                  <p><strong>Recovered A:</strong> {result.A}</p>

                  <h3>Terms Used</h3>
                  <ul>
                    {result.terms.map((term, index) => (
                      <li key={index}>
                        a{index + 1} = {term.a_i}, m{index + 1} = {term.m_i}, M{index + 1} = {term.M_i}, inverse = {term.inverse}, term = {term.term}
                      </li>
                    ))}
                  </ul>
                </>
              )}

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

export default CRTTab;