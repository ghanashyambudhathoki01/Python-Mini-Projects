<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body style="font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 20px; line-height: 1.6;">
  <h1>🔐 Password Generator - Python Project</h1>
  <p>A simple and secure terminal-based Python application that generates strong, random passwords based on user-defined criteria. Ensure your accounts are protected with passwords that are hard to guess and meet modern security standards.</p>

  <h2>📌 How It Works</h2>
  <ul>
    <li>The program asks the user for a desired password length (minimum 8 characters).</li>
    <li>It includes uppercase, lowercase, digits, and special characters based on user input.</li>
    <li>A random password is generated using secure methods.</li>
    <li>The password is validated and its <strong>entropy</strong> (strength) is calculated.</li>
    <li>You can optionally check the password against a list of weak/common passwords.</li>
  </ul>

  <h2>🎮 Features</h2>
  <h3>✅ Core Features</h3>
  <ul>
    <li>🔐 Custom password length</li>
    <li>🔡 Choose character types (uppercase, lowercase, digits, symbols)</li>
    <li>🧮 Calculates password entropy</li>
    <li>📛 Warns against weak/common patterns</li>
    <li>🔁 Regenerate multiple passwords quickly</li>
  </ul>

  <h3>⚙️ Advanced (Optional)</h3>
  <ul>
    <li>🧠 Secure random generation using <code>secrets</code> module</li>
    <li>🗂️ Wordlist-based validation (e.g. <code>500-worst-passwords.txt</code>)</li>
    <li>🔎 Entropy bits show how strong your password is</li>
    <li>📜 Clean CLI interface with prompt-based interaction</li>
  </ul>

  <h2>🧑‍💻 How to Use</h2>
  <ol>
    <li><strong>Run the script using Python:</strong>
      <pre><code>python password_generator.py</code></pre>
    </li>
    <li><strong>Follow the prompts:</strong>
      <pre><code>
Enter password length [>=8]: 12
Include uppercase? (y/n): y
Include lowercase? (y/n): y
Include digits? (y/n): y
Include punctuation? (y/n): y
      </code></pre>
    </li>
    <li><strong>Receive your secure password:</strong>
      <pre><code>
Generated password: Kf7@w#Lp9Qs%
      </code></pre>
    </li>
  </ol>

  <h2>📂 Requirements</h2>
  <ul>
    <li>✅ Python 3.x</li>
    <li>❌ No external libraries required — pure Python!</li>
  </ul>

  <h2>📸 Sample Output</h2>
  <pre><code>
Welcome to the Password Generator!
-------------------------------
Enter password length [>=8]: 14
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y

Generated Password: jK4#tL9z$Rq1Bw
Password Entropy: 81.7 bits
✅ Strong password.
  </code></pre>

  <h2>🧑‍🎓 Made With ❤️ by <a href="https://github.com/ghanashyambudhathoki01" target="_blank">Ghanashyam Budhathoki</a></h2>
</body>
</html>
