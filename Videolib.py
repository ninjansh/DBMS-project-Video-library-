import sqlite3

def create_connection():
    connection = sqlite3.connect('video_library.db')
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            year INTEGER,
            director TEXT
        )
    ''')
    connection.commit()

# Initialize database and table
conn = create_connection()
create_table(conn)
conn.close()
# Create a new video
def add_video(connection, title, genre, year, director):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO videos (title, genre, year, director) VALUES (?, ?, ?, ?)
    ''', (title, genre, year, director))
    connection.commit()

# Read all videos
def view_videos(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM videos')
    rows = cursor.fetchall()
    return rows

# Update video information
def update_video(connection, video_id, title, genre, year, director):
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE videos
        SET title = ?, genre = ?, year = ?, director = ?
        WHERE id = ?
    ''', (title, genre, year, director, video_id))
    connection.commit()

# Delete a video
def delete_video(connection, video_id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    connection.commit()
def main():
    conn = create_connection()
    
    while True:
        print("\nVideo Library Management System")
        print("1. Add Video")
        print("2. View Videos")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter title: ")
            genre = input("Enter genre: ")
            year = int(input("Enter year: "))
            director = input("Enter director: ")
            add_video(conn, title, genre, year, director)
            print("Video added successfully.")
        
        elif choice == '2':
            videos = view_videos(conn)
            for video in videos:
                print(f"ID: {video[0]}, Title: {video[1]}, Genre: {video[2]}, Year: {video[3]}, Director: {video[4]}")
        
        elif choice == '3':
            video_id = int(input("Enter video ID to update: "))
            title = input("Enter new title: ")
            genre = input("Enter new genre: ")
            year = int(input("Enter new year: "))
            director = input("Enter new director: ")
            update_video(conn, video_id, title, genre, year, director)
            print("Video updated successfully.")
        
        elif choice == '4':
            video_id = int(input("Enter video ID to delete: "))
            delete_video(conn, video_id)
            print("Video deleted successfully.")
        
        elif choice == '5':
            conn.close()
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
