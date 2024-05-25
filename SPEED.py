import time

#get the timestamp before inference in seconds
start_ts = time.time()

#Predict the response for test dataset. I want to measure the speed of this prediction here.
y_pred = clf.predict(X_test)

#get the timestamp after the inference in second
end_ts = time.time()

# print the time difference in between start and end timestamps in seconds
print(f"Prediction Time [s]: {(end_ts-start_ts):.3f}")
