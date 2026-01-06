// // const express = require('express');
// // const path = require('path');
// // const app = express();

// // app.use(express.static('templates')); // Aapki index.html yahan se load hogi

// // // Vercel ke liye serverless function setup
// // app.get('/', (req, res) => {
// //     res.sendFile(path.join(__dirname, 'templates', 'index.html'));
// // });

// // const PORT = process.env.PORT || 3000;
// // app.listen(PORT, () => console.log(`Server running on port ${PORT}`));



// const express = require('express');
// const path = require('path');
// const app = express();
// // index.js ke andar spawn logic
// const pythonProcess = spawn('python3', [path.join(__dirname, 'billing.py'), userEmail]);

// // Behtar tariqa: Absolute path use karein
// app.use(express.static(path.join(__dirname, 'templates')));

// app.get('/', (req, res) => {
//     res.sendFile(path.join(__dirname, 'templates', 'index.html'));
// });

// // Ye line cPanel aur Vercel dono ke liye zaroori hai
// const PORT = process.env.PORT || 3000;
// app.listen(PORT, () => console.log(`Server running on port ${PORT}`));


// Aapka code ab bilkul sahi direction mein hai, lekin aik choti si technical cheez reh gayi hai. spawn function ko istemal karne ke liye aapko use child_process se import karna zaroori hai, warna Node.js ko pata nahi chalega ke spawn kya hai.

// Aapki final index.js bilkul aisi honi chahiye (copy-paste kar lein):
// update code 5 jan ko billing system wali requirement ko fullfill krny ky lea bki code blkul sahi km kr ra ha 


const express = require('express');
const path = require('path');
const { spawn } = require('child_process'); // Ye line zaroori hai!
const app = express();

app.use(express.json()); // JSON request handle karne ke liye

// Static files (CSS/JS) ke liye
app.use(express.static(path.join(__dirname, 'templates')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'index.html'));
});

// Chat endpoint jahan user email likhega
app.post('/api/chat', (req, res) => {
    const userMessage = req.body.message;
    const emailRegex = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/;
    const foundEmail = userMessage.match(emailRegex);

    if (foundEmail) {
        const userEmail = foundEmail[0];
        // billing.py root mein hai isliye path simple rakha hai
        const pythonProcess = spawn('python3', [path.join(__dirname, 'billing.py'), userEmail]);

        pythonProcess.stdout.on('data', (data) => {
            try {
                const billingData = JSON.parse(data.toString());
                res.json({ 
                    reply: `✅ **Account Info:**\nName: ${billingData.name}\nPlan: ${billingData.service}\nStatus: ${billingData.status}` 
                });
            } catch (e) {
                res.json({ reply: "❌ Email database mein nahi mili." });
            }
        });
    } else {
        res.json({ reply: "Billing check karne ke liye apna registered email likhein." });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));