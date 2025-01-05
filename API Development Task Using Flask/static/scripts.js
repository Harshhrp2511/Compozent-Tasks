// Fetch and display tasks
async function fetchTasks() {
    const response = await fetch('/api/tasks');
    const tasks = await response.json();

    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';

    tasks.forEach(task => {
        const taskItem = document.createElement('div');
        taskItem.className = 'task-item';
        taskItem.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>
            <p>Status: ${task.completed ? 'Completed' : 'Incomplete'}</p>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(taskItem);
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
}

// Delete a task
async function deleteTask(taskId) {
    await fetch(`/api/tasks/${taskId}`, {
        method: 'DELETE'
    });

    fetchTasks();
}

// Initial fetch of tasks
fetchTasks();
