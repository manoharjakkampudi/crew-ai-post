import warnings
warnings.filterwarnings("ignore")

import yaml
from crewai import Task

def load_tasks(agents: dict, path='config/tasks.yaml'):
    with open(path, 'r') as f:
        task_config = yaml.safe_load(f)

    tasks = []
    for agent_id, task_info in task_config.items():
        agent = agents.get(agent_id)
        if not agent:
            raise ValueError(f"Agent '{agent_id}' not found for task config.")

        tasks.append(Task(
            description=task_info['description'],
            expected_output=task_info['expected_output'],
            agent=agent
        ))

    return tasks
