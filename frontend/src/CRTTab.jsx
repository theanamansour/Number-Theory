import { useState } from "react";
import "./App.css";
import {

const API_BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
  Grid,
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

function CRTTab() {
  const [mode, setMode] = useState("A_to_residues");

  const [A, setA] = useState("");
  const [moduli, setModuli] = useState("");
  const [residues, setResidues] = useState("");

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const parseNumberList = (text) =>
    text
      .split(",")
      .map((item) => item.trim())
      .filter((item) => item !== "")
      .map(Number);

  const loadAtoResiduesExample = () => {
    setMode("A_to_residues");
    setA("23");
    setModuli("3,5,7");
    setResidues("");
    setResult(null);
    setError("");
    setCopied(false);
  };

  const loadResiduesToAExample = () => {
    setMode("residues_to_A");
    setA("");
    setResidues("2,3,1");
    setModuli("3,5,7");
    setResult(null);
    setError("");
    setCopied(false);
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

        response = await fetch(`${API_BASE}/api/crt/residues`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...getAuthHeaders(),
          },
          body: JSON.stringify({
            A: Number(A),
            moduli: moduliList,
          }),
        });
      } else {
        const residuesList = parseNumberList(residues);

        if (residuesList.length === 0 || residuesList.some(isNaN)) {
          setError("Please enter valid residues.");
          return;
        }

        if (residuesList.length !== moduliList.length) {
          setError("Residues and moduli must match.");
          return;
        }

        response = await fetch(`${API_BASE}/api/crt/recover`, {
          method: "POST",
          headers: { 
            "Content-Type": "application/json",
            ...getAuthHeaders(),
           },
          body: JSON.stringify({
            residues: residuesList,
            moduli: moduliList,
          }),
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
      <main className="module-container">
        <div className="card">
          <div className="tool-grid">

            {/* LEFT SIDE */}
            <div className="tool-left">

              <div className="tool-title">
                <div className="tool-icon">
                  <Grid size={30} strokeWidth={2.2} />
                </div>
                <div>
                  <h3>Chinese Remainder Theorem</h3>
                  <p>Solve modular systems or compute residues.</p>
                </div>
              </div>

              {/* MODE SWITCH */}
              <div className="button-row">
                <button
                  className={mode === "A_to_residues" ? "" : "secondary"}
                  onClick={() => setMode("A_to_residues")}
                >
                  A → Residues
                </button>

                <button
                  className={mode === "residues_to_A" ? "" : "secondary"}
                  onClick={() => setMode("residues_to_A")}
                >
                  Residues → A
                </button>
              </div>

              {/* INPUTS */}
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
                    placeholder="Enter moduli (e.g. 3,5,7)"
                  />
                </>
              )}

              {mode === "residues_to_A" && (
                <>
                  <input
                    type="text"
                    value={residues}
                    onChange={(e) => setResidues(e.target.value)}
                    placeholder="Enter residues (e.g. 2,3,1)"
                  />

                  <input
                    type="text"
                    value={moduli}
                    onChange={(e) => setModuli(e.target.value)}
                    placeholder="Enter moduli (e.g. 3,5,7)"
                  />
                </>
              )}

              <div className="input-tip">
                <Lightbulb size={14} />
                <span>Tip: Moduli must be pairwise coprime.</span>
              </div>

              <div className="button-row">
                <button onClick={handleCRT}>
                  <Rocket size={16} />
                  Compute CRT
                </button>

                <button className="secondary" onClick={handleClear}>
                  <RotateCcw size={16} />
                  Clear
                </button>
              </div>
            </div>

            {/* RIGHT SIDE */}
            <div className="tool-right">

              <div className="examples-title">
                <Star size={14} />
                <span>Try these examples</span>
              </div>

              <div className="example-row crt-row">
                <button
                  type="button"
                  className="example-chip crt-chip"
                  onClick={loadAtoResiduesExample}
                >
                  A = 23 mod (3,5,7)
                </button>

                <button
                  type="button"
                  className="example-chip crt-chip"
                  onClick={loadResiduesToAExample}
                >
                  (2,3,1) mod (3,5,7)
                </button>
              </div>

              <div className="info-box">
                <div className="info-title">
                  <div className="info-icon">
                    <Info size={14} />
                  </div>
                  <h4>What is CRT?</h4>
                </div>

                <p>
                  The Chinese Remainder Theorem solves systems of congruences
                  and guarantees a unique solution modulo the product of moduli.
                </p>
              </div>
            </div>

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
                  <p><strong>Recovered A:</strong> {result.A}</p>
                </>
              )}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default CRTTab;
