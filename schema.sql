CREATE TABLE IF NOT EXISTS bugs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    reported_by TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Created'
        CHECK(status IN ('Created', 'In Progress', 'Done')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);