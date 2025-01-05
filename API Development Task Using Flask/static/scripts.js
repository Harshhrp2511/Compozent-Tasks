// Fetch and display tasks
async function fetchTasks() {
    const response = await fetch('/api/tasks');
    const tasks = await response.json();

    const taskContainer = document.getElementById('tasks-container');
    taskContainer.innerHTML = '';

    tasks.forEach(task => {
        const taskItem = document.createElement('div');
        taskItem.className = 'task-item';
        taskItem.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>
            <p>Status: ${task.completed ? 'Completed' : 'Incomplete'}</p>
            <div class="actions">
                <button class="action-btn" onclick="markComplete(${task.id}, ${!task.completed})">
                    ${task.completed ? 'Mark Incomplete' : 'Mark Complete'}
                </button>
                <button class="action-btn" onclick="copyToClipboard('${task.title}', '${task.description}')">Copy</button>
                <button class="action-btn" onclick="deleteTask(${task.id})">Delete</button>
            </div>
        `;
        taskContainer.appendChild(taskItem);
    });
}

// Add a new task
async function addTask() {
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-desc').value;

    if (!title || !description) {
        alert('Please fill in all fields!');
        return;
    }

    await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description })
    });

    fetchTasks();
    clearForm();
}

// Mark a task as complete or incomplete
async function markComplete(taskId, completed) {
    await fetch(`/api/tasks/${taskId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed })
    });

    fetchTasks();
}

// Delete a task
async function deleteTask(taskId) {
    await fetch(`/api/tasks/${taskId}`, {
        method: 'DELETE'
    });

    fetchTasks();
}

// Copy task details to clipboard
function copyToClipboard(title, description) {
    const text = `Task: ${title}\nDescription: ${description}`;
    navigator.clipboard.writeText(text).then(() => {
        alert('Task copied to clipboard!');
    });
}

// Clear input fields
function clearForm() {
    document.getElementById('task-title').value = '';
    document.getElementById('task-desc').value = '';
}

// Initial fetch of tasks
fetchTasks();
