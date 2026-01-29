const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const generateBtn = document.getElementById('generateBtn');
const btnText = generateBtn.querySelector('.btn-text');
const loader = generateBtn.querySelector('.loader');

async function generateTestCases() {
    const text = userInput.value.trim();
    if (!text) return;

    // Add user message
    addMessage(text, 'user');
    userInput.value = '';

    // UI state loading
    setLoading(true);

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: text })
        });

        const data = await response.json();

        if (response.ok) {
            renderTestCases(data);
        } else {
            addMessage(`Error: ${data.detail || 'Failed to generate test cases'}`, 'system');
        }
    } catch (error) {
        addMessage(`Network Error: ${error.message}`, 'system');
    } finally {
        setLoading(false);
    }
}

function setLoading(isLoading) {
    generateBtn.disabled = isLoading;
    if (isLoading) {
        btnText.classList.add('hidden');
        loader.classList.remove('hidden');
    } else {
        btnText.classList.remove('hidden');
        loader.classList.add('hidden');
    }
}

function addMessage(text, role) {
    const div = document.createElement('div');
    div.className = `message ${role}`;
    div.innerHTML = `<div class="bubble">${text}</div>`;
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function renderTestCases(data) {
    const systemDiv = document.createElement('div');
    systemDiv.className = 'message system';

    // Stringify data for the onclick handler safely
    const dataStr = encodeURIComponent(JSON.stringify(data));

    let html = `<div class="bubble">
        <div class="message-header">
            <strong>Summary:</strong> ${data.summary}
            <button class="copy-btn" onclick="copyAsMarkdown('${dataStr}')">Copy MD</button>
        </div>
        <div class="test-cases-list">`;

    data.test_cases.forEach(tc => {
        const priorityClass = `priority-${tc.priority.toLowerCase()}`;
        html += `
        <div class="test-case-card">
            <h4>${tc.id}: ${tc.title}</h4>
            <p><strong>Preconditions:</strong> ${tc.preconditions}</p>
            <p><strong>Steps:</strong></p>
            <ul>${tc.steps.map(s => `<li>${s}</li>`).join('')}</ul>
            <p><strong>Expected:</strong> ${tc.expected_result}</p>
            <p><strong>Priority:</strong> <span class="${priorityClass}">${tc.priority}</span></p>
        </div>`;
    });

    html += `</div></div>`;
    systemDiv.innerHTML = html;
    chatContainer.appendChild(systemDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function copyAsMarkdown(dataEncoded) {
    const data = JSON.parse(decodeURIComponent(dataEncoded));
    let md = `# Test Suite: ${data.summary}\n\n`;
    data.test_cases.forEach(tc => {
        md += `## ${tc.id}: ${tc.title}\n`;
        md += `**Priority:** ${tc.priority}\n`;
        md += `**Preconditions:** ${tc.preconditions}\n`;
        md += `**Steps:**\n${tc.steps.map(s => `1. ${s}`).join('\n')}\n`;
        md += `**Expected Result:** ${tc.expected_result}\n\n---\n\n`;
    });

    navigator.clipboard.writeText(md).then(() => {
        const btn = event.target;
        const originalText = btn.innerText;
        btn.innerText = 'Copied!';
        setTimeout(() => btn.innerText = originalText, 2000);
    });
}

generateBtn.addEventListener('click', generateTestCases);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        generateTestCases();
    }
});
