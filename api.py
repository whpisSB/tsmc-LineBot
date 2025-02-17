import requests

ENDPOINT = ''

def get_review_history(user_id):
    res = requests.get(f'{ENDPOINT}/review_history', json={'line_id': user_id})
    data = res.json()

    message = ""
    
    if res.status_code == 200:
        
        message += "台積點: " + str(data[0]['total_points']) + "\n\n"

        review_history = []
        if len(data) > 1:
            for i, review in enumerate(data[1:], 1):
                message += f"{i}. 審核時間: {review['review_at']}\n   PR連結: {review['pr_url']}\n   審核者: {review['reviewer_github_id']}\n   得分: {review['points']}\n\n"
        else:
            message = "目前沒有審核紀錄"
            
    return message

def get_user_reward(user_id):
    res = requests.get(f'{ENDPOINT}/user_rewards', json={'line_id': user_id})
    print(res)
    rewards = res.json()
    return rewards if res.status_code == 200 else None

def get_reward_data():
    res = requests.get(f'{ENDPOINT}/reward')
    reward = res.json()
    print("====\n",reward)
    return reward if res.status_code == 200 else None

def exchange_reward(user_id, reward_id):
    body = {
        'line_id': user_id,
        'reward_id': reward_id
    }
    
    res = requests.post(f'{ENDPOINT}/exchange_reward', json=body)

    return "購買成功" if res.status_code == 200 else "點數不足"

def generate_icon(user_id, prompt):
    body = {
        'line_id': user_id,
        'prompt': prompt
    }

    res = requests.post(f'{ENDPOINT}/icon', json=body)
    print(res)
    icon = res.json()
    return icon['url'] if res.status_code == 200 else None

def send_review_result(data, result):
    body = {
        'author_id': data['author_id'],
        'pr_url': data['pr_url'],
        'reviewer_id': data['reviewer_id'],
        'result': result
    }

    res = requests.post(f'{ENDPOINT}/review', json=body)

    return "回覆成功" if res.status_code == 200 else "回覆失敗"
