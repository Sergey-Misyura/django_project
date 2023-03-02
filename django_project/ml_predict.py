def prediction_model(review):
    features = [review]
    if features !=[]:
        labels_dict = {0: 1, 1: 10, 2: 2, 3: 3, 4: 4, 5: 7, 6: 8, 7: 9}
        import tensorflow as tf

        reconstructed_model = tf.keras.models.load_model('/home/SergeyM/django_project/end_to_end_model_LSTM2')
        prediction = reconstructed_model.predict(features)

        rating = labels_dict[int(tf.math.argmax(prediction[0]))]
        status = 'Отрицательный' if 1<=rating<=4 else 'Положительный'

        return f'Рейтинг фильма по отзыву: {rating} звёзд.\nСтатус отзыва:  {status}.'

    return 'Ошибка. Введите отзыв.'
