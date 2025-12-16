def predict_rating(model,user_id, item_id):
    prediction = model.predict(user_id,item_id)
    return prediction.est

def recommend_top_n(model, user_id, trainset, n = 5):
    items = [trainset.to_raw_iid(i) for i in trainset.all_items()]

    predictions = [
        (item, predict_rating(model,user_id,item))
        for item in items
    ]
    predictions.sort(key = lambda x : x[1], reverse = True)
    return predictions[:n]
