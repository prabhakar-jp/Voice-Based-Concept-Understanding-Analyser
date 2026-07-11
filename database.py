import sqlite3

def create_database():
    conn = sqlite3.connect("database/vbcua.db")
    cursor = conn.cursor()

    # USER TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        role TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # AUDIO FILE TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audio_file (
        audio_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        file_name TEXT,
        file_path TEXT,
        duration_sec REAL,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT,
        FOREIGN KEY(user_id) REFERENCES user(user_id)
    )
    """)

    # TRANSCRIPT TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transcript (
        transcript_id INTEGER PRIMARY KEY AUTOINCREMENT,
        audio_id INTEGER,
        transcript_text TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(audio_id) REFERENCES audio_file(audio_id)
    )
    """)

    # REFERENCE CONCEPT TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reference_concept (
        ref_concept_id INTEGER PRIMARY KEY AUTOINCREMENT,
        concept_title TEXT,
        concept_text TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # SEMANTIC SIMILARITY TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS semantic_similarity (
        similarity_id INTEGER PRIMARY KEY AUTOINCREMENT,
        transcript_id INTEGER,
        ref_concept_id INTEGER,
        similarity_score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(transcript_id) REFERENCES transcript(transcript_id),
        FOREIGN KEY(ref_concept_id) REFERENCES reference_concept(ref_concept_id)
    )
    """)

    # AUDIO FEATURE TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audio_feature (
        feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
        audio_id INTEGER,
        pause_ratio REAL,
        rms_energy REAL,
        zero_crossing_rate REAL,
        duration_sec REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(audio_id) REFERENCES audio_file(audio_id)
    )
    """)

    # EVALUATION RESULT TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluation_result (
        result_id INTEGER PRIMARY KEY AUTOINCREMENT,
        audio_id INTEGER,
        ref_concept_id INTEGER,
        overall_score REAL,
        understanding_level TEXT,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(audio_id) REFERENCES audio_file(audio_id),
        FOREIGN KEY(ref_concept_id) REFERENCES reference_concept(ref_concept_id)
    )
    """)

    # REPORT TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS report (
        report_id INTEGER PRIMARY KEY AUTOINCREMENT,
        result_id INTEGER,
        pdf_path TEXT,
        generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        file_size_kb INTEGER,
        FOREIGN KEY(result_id) REFERENCES evaluation_result(result_id)
    )
    """)

    # SESSION TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS session (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        started_at TIMESTAMP,
        ended_at TIMESTAMP,
        status TEXT,
        FOREIGN KEY(user_id) REFERENCES user(user_id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
    