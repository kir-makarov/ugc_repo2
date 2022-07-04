db.auth('team2', 'admin')

db = db.getSiblingDB('movies')

db.createUser({
  user: 'team2',
  pwd: 'team2',
  roles: [
    {
      role: 'root',
      db: 'admin',
    },
  ],
});