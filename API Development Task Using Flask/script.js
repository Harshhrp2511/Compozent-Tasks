const taskList = document.getElementById('task-list');
const taskInput = document.getElementById('task-input');

function loadTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            taskList.innerHTML = '';
            tasks.forEach(task => {
                const taskItem = document.createElement('li');
                taskItem.textContent = task.task;
                taskList.appendChild(taskItem);
            });
        });
}

function addTask() {
    const task = taskInput.value;
    if (task) {
        fetch('/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ task: task })
        })
            .then(response => response.json())
            .then(() => {
                loadTasks();
                taskInput.value = '';
            });
    }
}

// Load tasks on page load
window.onload = loadTasks;
