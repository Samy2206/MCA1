from pymongo import MongoClient, errors
# Replace with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017")
db = client['mydatabase']
# Collections to perform operations on
collection1 = db['collection1']
# Start a session
session = client.start_session()
# Start a transaction
try:
    session.start_transaction()
    # Perform some operations
    collection1.insert_one({'_id': 1, 'name': 'Alice'})
    collection1.insert_one({'_id': 1, 'role': 'Engineer'})
    # Commit the transaction
    session.commit_transaction()
    print("Transaction committed successfully.")
except errors.DuplicateKeyError as e:
    # Handle duplicate key error (or other exceptions)
    print(f"Transaction aborted due to: {e}")
    session.abort_transaction()
except Exception as e:
    # Rollback for any other exception
    print(f"An error occurred: {e}")
    session.abort_transaction()
finally:
    #end the session
    session.end_session()