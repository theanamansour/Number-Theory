import "./App.css";

function App() {
  return (
    <div className="app">
      <header className="hero">
        <h1>Number Theory Web Application</h1>
        <p>
          An educational cryptography toolkit for prime factorization, Euler’s
          totient function, Miller–Rabin primality testing, fast modular
          exponentiation, and the Chinese Remainder Theorem.
        </p>
      </header>

      <main className="modules">
        <div className="card">
          <h2>Prime Factorization</h2>
          <p>Break an integer into its prime factors with step-by-step output.</p>
        </div>

        <div className="card">
          <h2>Euler’s Totient</h2>
          <p>Compute φ(n) and explain how the result is derived.</p>
        </div>

        <div className="card">
          <h2>Miller–Rabin</h2>
          <p>Test whether a number is composite or probably prime.</p>
        </div>

        <div className="card">
          <h2>Fast Modular Exponentiation</h2>
          <p>Efficiently compute a^b mod m with algorithm steps.</p>
        </div>

        <div className="card">
          <h2>Chinese Remainder Theorem</h2>
          <p>Solve congruence systems or compute residues from a number.</p>
        </div>
      </main>
    </div>
  );
}

export default App;