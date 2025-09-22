# Topic: Alembic Database Migration Tool

## Outline

1. What is Alembic and why use it
2. Install Alembic
3. Initialize Alembic project
4. Configure Alembic files
5. Create revision (migration file)
6. Write upgrade and downgrade functions
7. Run upgrade migration
8. Run downgrade migration
9. Update application for phone number feature

---

## 1. What is Alembic and why use it

Alembic is a tool that helps you **change database tables** safely **without losing data**.

---

### ⚠️ Problem without Alembic:

You already have a `users` table like this:

```
+----+------------------+------------+-----------+----------+
| id | email            | first_name | last_name | password |
+----+------------------+------------+-----------+----------+
| 1  | test@mail.com    | Ali        | Khan      | 1234     |
+----+------------------+------------+-----------+----------+

```

Now you want to **add phone_number column**.

👉 Without Alembic, SQLAlchemy cannot update existing tables.

It will try to drop and recreate the table (❌ you lose old data).

---

### ✅ Solution with Alembic:

Alembic allows you to **upgrade** the database safely:

```
Before:
+----+------------------+------------+-----------+----------+
| id | email            | first_name | last_name | password |
+----+------------------+------------+-----------+----------+

After Alembic upgrade:
+----+------------------+------------+-----------+----------+--------------+
| id | email            | first_name | last_name | password | phone_number |
+----+------------------+------------+-----------+----------+--------------+
| 1  | test@mail.com    | Ali        | Khan      | 1234     | NULL         |
+----+------------------+------------+-----------+----------+--------------+

```

👉 Old data is safe.

👉 New column `phone_number` is added.

---

💡 **In short:**

- SQLAlchemy = create new tables
- Alembic = update existing tables

---

- Alembic is a lightweight database migration tool for SQLAlchemy
- Migration tools allow us to plan, transfer and upgrade resources within database
- Alembic allows you to change SQLAlchemy database table after it has already been created
- SQLAlchemy only creates new database tables, not enhance existing ones
- Alembic lets you add columns to database table without deleting table or data
- Provides creation and invocation of change management scripts
- Allows creating migration environments and changing data

**Example Problem:**

- Current users table has: ID, email, first_name, last_name, hashed_password
- Want to add phone_number column to existing data
- Without Alembic: would need to delete table and lose all data

## 2. Install Alembic

---

## Install Alembic

1. Open your terminal (command prompt / shell).
2. Run this command:

```bash
pip install alembic

```

This will download and install Alembic on your system.

---

### Check if installed:

Type in terminal:

```bash
alembic --version

```

If it shows a version number (like `alembic 1.13.2`), that means Alembic is ready to use ✅

---

👉 Now you try this step.

When it’s done, reply **ok done** so we move to **Step 3 (Initialize Alembic project)**.

**Alembic Commands Overview:**

- `alembic init [folder_name]` - Initialize new environment
- `alembic revision -m "message"` - Create new revision file
- `alembic upgrade [revision_id]` - Run upgrade migration
- `alembic downgrade -1` - Downgrade last migration

## 3. Initialize Alembic project

---

After installing Alembic, you need to **initialize** it in your project.

This will create all the files Alembic needs.

Run this command in your project folder:

```bash
alembic init alembic

```

---

### 📂 What this will create?

1. **`alembic.ini`** → main Alembic config file (ile - Configuration file that Alembic looks for when invoked)
2. **`alembic/` folder** → will store migration scripts (Contains environmental properties, holds all revisions)
   - inside this folder, you’ll see:
     - `env.py` (environment settings)
     - `script.py.mako` (template)
     - `versions/` (all migration files will be saved here)

---

So after init, your project looks like:

```
my_project/
│── alembic.ini
│── alembic/
│    ├── env.py
│    ├── script.py.mako
│    └── versions/   (empty for now)
│── models.py
│── main.py

```

---

## 4. Configure Alembic files

Now we need to **connect Alembic with your database + models**.

---

### 1. Edit `alembic.ini`

Open `alembic.ini` file.

Find this line (around line ~63):

```
sqlalchemy.url = driver://user:pass@localhost/dbname

```

👉 Replace it with your database URL.

Example (for SQLite):

```
sqlalchemy.url = sqlite:///./todosapp.db

```

If you are using PostgreSQL/MySQL, the URL will be different, like:

```
sqlalchemy.url = postgresql://username:password@localhost/mydb

```

---

### 2. Edit `alembic/env.py`

Now open `alembic/env.py`.

- At the top, import your models:

```python
import models

```

- if mainfolder > folder > models > alambic
  ![image.png](attachment:c150a137-d343-4832-9111-af983d7a928f:image.png)
  ```python
  from todoapp import models

  ```
- Then, find this line:

```python
target_metadata = None

```

👉 Replace with:

```python
target_metadata = models.Base.metadata

```

This tells Alembic: _“Use SQLAlchemy models from models.py to track changes.”_

and remove this :

```
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
```

add this only:

```python
fileConfig(config.config_file_name)
```

---

## 5. Create revision (migration file)

---

### Why do we need this?

Think of Alembic like a **history book** for your database.

- Every time you want to change the database (add column, remove column, etc.),
  👉 you must write that change in a **new migration file**.
- This file is like a “chapter” that says:
  - `upgrade()` → how to apply the change (go forward)
  - `downgrade()` → how to undo the change (go backward)

So in our case:

We want to add **phone_number** column to the `users` table → so we need a new migration file for this.

That’s the perfect way to think about it.

- **Git commit** = saves code changes in history
- **Alembic revision (migration file)** = saves database changes in history

---

### What command to run

In your terminal, type:

```bash
alembic revision -m "add phone_number column to users"

```

---

### What happens after running?

Alembic will create a new file inside:

```
alembic/versions/

```

File name example:

```
3b1c2d4e5f6_add_phone_number_column_to_users.py

```

Inside it, you will see:

```python
def upgrade():
    pass   # we will write "add column" code here

def downgrade():
    pass   # we will write "remove column" code here

```

---

### 🔎 ASCII Visual

```
[Database changes]
     ↓
+--------------------+
| New Migration File |
|--------------------|
| upgrade()   -> add |
| downgrade() -> undo|
+--------------------+

```

👉 Right now it’s empty.

👉 In the **next step**, we will fill it with code to add/remove the column.

---

## 6. Write upgrade and downgrade functions

**File: [revision_id]\_create_phone_number_for_user_column.py**

---

### ❓ Why are we doing this?

In Step 5, Alembic created a **migration file** (like a Git commit file).

Right now that file is **empty** → it only has two functions:

```python
def upgrade():
    pass

def downgrade():
    pass

```

But we want this migration to **add a new column** (`phone_number`) to the `users` table.

So now we must **fill these functions** with real instructions.

- `upgrade()` → what to do when we apply this migration (add the column)
- `downgrade()` → what to do if we undo this migration (remove the column)

---

### How to do it

Open the new migration file (inside `alembic/versions/`).

Replace the functions with this code:

```python
from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    # Add a new column 'phone_number' to 'users' table
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))

def downgrade() -> None:
    # Remove the column if we roll back
    op.drop_column('users', 'phone_number')

```

---

### ASCII Visual

**Before upgrade:**

```
users table:
id | email | first_name | last_name | password

```

**After upgrade:**

```
users table:
id | email | first_name | last_name | password | phone_number

```

**After downgrade:**

```
users table:
id | email | first_name | last_name | password

```

---

---

## How Alembic Migration Works

### 1. Alembic creates a **migration file**

- You run:
  ```bash
  alembic revision -m "add phone_number"

  ```
- This creates a Python file with `upgrade()` and `downgrade()` functions.

---

### 2. You write **instructions** in that file

Example:

```python
def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String()))

def downgrade():
    op.drop_column('users', 'phone_number')

```

This is just Python code telling Alembic **what to do in SQL**.

---

### 3. Alembic translates it into **SQL commands**

When you run:

```bash
	alembic upgrade head

```

Alembic reads your Python code and converts it into SQL:

```sql
ALTER TABLE users ADD COLUMN phone_number VARCHAR;

```

👉 This command is sent to your database.

👉 Database adds the new column.

---

### 4. Alembic tracks history in a special table

Alembic keeps a hidden table in your database called **alembic_version**.

It looks like this:

```
alembic_version
---------------
3b1c2d4e5f6

```

This means: _“Your database is at migration 3b1c2d4e5f6”_.

So Alembic always knows which migrations are applied.

---

### 5. Downgrade works the same way

If you run:

```bash
alembic downgrade -1

```

Alembic looks at your `downgrade()` function → converts it to SQL → applies it:

```sql
ALTER TABLE users DROP COLUMN phone_number;

```

And updates the `alembic_version` table to go one step back.

---

### 🔎 ASCII Visual

```
You write code in migration file
       ↓
Alembic converts it to SQL
       ↓
Database runs SQL command
       ↓
alembic_version table updated

```

---

👉 So basically:

- **You write Python instructions**
- **Alembic turns them into SQL**
- **Database executes SQL**
- **Alembic remembers the state**

---

```bash
alembic downgrade -1

```

---

## ❓ What is `1` in Alembic?

- `1` means: **go back one step in migration history**.
- Alembic keeps a list of all migrations you applied (like Git commits).
- So if you just want to undo the **last migration**, you use `1`.

---

### Example

Imagine you have these migrations in order:

```
[1] create users table
[2] add email column
[3] add phone_number column   <-- current

```

If you run:

```bash
alembic downgrade -1

```

Alembic will undo **step 3** (remove the `phone_number` column).

Now your database is back at step 2.

---

### You can also use specific revision IDs

Instead of `-1`, you can use the unique revision ID that Alembic created.

Example:

```bash
alembic downgrade 2b6c1f3e4d5

```

That will downgrade back to the state of that specific migration.

---

### 🔎 ASCII Visual

```
Migrations history:
[1] ----> [2] ----> [3]

`alembic downgrade -1`
means go back:
[1] ----> [2]

```

---

👉 So simply:

- `upgrade head` = go to the latest migration
- `downgrade -1` = undo the last migration

---

---

## 🔹 How to jump to a specific migration

### 1. Find the migration ID

Each migration file in `alembic/versions/` starts with a unique **revision ID**. Example:

```
alembic/versions/
    2b6c1f3e4d5_add_email_column.py
    3c7a2b9f8d1_add_phone_number.py

```

Here:

- `2b6c1f3e4d5` is the ID of the _email column_ migration
- `3c7a2b9f8d1` is the ID of the _phone_number_ migration

---

### 2. Upgrade (jump forward) to a specific migration

```bash
alembic upgrade 2b6c1f3e4d5

```

➡️ This applies migrations **up to that ID**.

---

### 3. Downgrade (jump backward) to a specific migration

```bash
alembic downgrade 2b6c1f3e4d5

```

➡️ This removes migrations **until your DB is at that ID**.

---

### 4. Special keywords

- `head` → the latest migration (like Git `master` / `main`)
- `base` → go back to the very first state (no migrations applied)
- `+2` → move forward by 2 steps
- `2` → move backward by 2 steps

---

### 🔎 ASCII Example

```
(base) → [1] create users
          ↓
        [2] add email
          ↓
        [3] add phone_number

```

- `alembic upgrade head` → goes to [3]
- `alembic downgrade -1` → goes back to [2]
- `alembic downgrade base` → goes back to nothing (empty DB)
- `alembic upgrade 2b6c1f3e4d5` → jumps exactly to [2]

---

---

---

## 7. Run upgrade migration

### ❓ Why are we doing this?

Until now, we only **wrote instructions** in the migration file (upgrade + downgrade).

But the database itself is still unchanged.

Now we need to **apply (execute)** that migration so the database structure is updated.

- Run upgrade with revision ID:

```bash
alembic upgrade [revision_id]

#alembic upgrade 23223232

```

**Result:**

- Adds phone_number column to users table
- All existing data remains intact
- New column is nullable=True (shows as null for existing users)

---

### How to run

In your terminal, run:

```bash
alembic upgrade head

```

- `upgrade` → tells Alembic: _“Apply migrations”_
- `head` → means _“Go to the latest migration file available”_

---

### What happens internally

1. Alembic checks your `alembic/versions/` folder
2. Finds the latest migration file
3. Runs the `upgrade()` function inside it

   → which adds the `phone_number` column

---

### Before vs After

**Before upgrade (users table):**

```
id | email | first_name | last_name | password

```

**After upgrade (users table):**

```
id | email | first_name | last_name | password | phone_number

```

Old data is safe, new column added with `NULL` values.

---

✅ Now your database has the `phone_number` column 🎉

---

## ❓ What is `head` in Alembic?

## ❓ What is `head` in Alembic?

Think of migrations like a **chain of commits** (just like Git).

Example history:

```
[rev1] create users table
[rev2] add email column
[rev3] add phone_number column   <-- latest (HEAD)

```

- **`head`** means → the **latest migration** in this chain.
- When you run:
  ```bash
  alembic upgrade head

  ```
  Alembic will apply **all migrations up to the latest one** (rev3 here).

---

### 🔎 ASCII Visual

```
rev1  →  rev2  →  rev3
                  ↑
                 HEAD

```

- `upgrade head` → go forward to the latest
- `downgrade -1` → go back one step from head

---

💡 In short:

- `head` = newest migration
- `base` = very first empty state (before any migrations)

---

Do you want me to also show you how **multiple heads** can exist (when branches happen), or keep it simple with just one head for now?

---

## 8. Run downgrade migration

- To revert last migration:

```bash
alembic downgrade -1

```

**Result:**

- Removes phone_number column from users table
- 1 means revert the last migration

### ❓ Why are we doing this?

Sometimes you make a mistake in a migration (wrong column name, wrong type, etc.).

In that case, you need to **undo (rollback)** the last change.

That’s where **`downgrade`** comes in → it runs the `downgrade()` function you wrote earlier.

---

### ✅ How to run

```bash
alembic downgrade -1

```

- `downgrade` → go backward in history
- `1` → go back **one step** (undo the last migration)

---

### What happens internally

1. Alembic checks the latest migration (the `head`)
2. Runs the `downgrade()` function

   → which removes the `phone_number` column

---

### Before vs After

**Before downgrade (users table):**

```
id | email | first_name | last_name | password | phone_number

```

**After downgrade (users table):**

```
id | email | first_name | last_name | password

```

👉 The database is back to its earlier state.

---

⚠️ Note: Only use downgrade if really needed (like fixing bugs).

Most of the time, we keep upgrading forward.

---

## 9. Update application for phone number feature

### ❓ Why are we doing this?

We changed the **database schema** (added `phone_number` column).

But our **application code** (models, APIs) still doesn’t know about this new column.

So now we must update our **SQLAlchemy models** and **API endpoints**.

---

### ✅ How to update

### 1. Update `models.py`

Add the new column in your `Users` model:

```python
from sqlalchemy import Column, String

class Users(Base):
    __tablename__ = "users"

    # existing columns...
    phone_number = Column(String, nullable=True)

```

---

### 2. Update user creation request (`CreateUserRequest`)

In your Pydantic schema (example `auth.py`):

```python
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    role: str
    password: str
    phone_number: str   # <-- new field

```

---

### 3. Update user creation logic

When saving new user:

```python
create_user_model = Users(
    email=create_user_request.email,
    username=create_user_request.username,
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    role=create_user_request.role,
    hashed_password=hash_password,
    is_active=True,
    phone_number=create_user_request.phone_number   # <-- new field
)

```

---

### 4. Add endpoint to update phone number

In `users.py`:

```python
@router.put("/phone_number/{phone_number}")
async def change_phone_number(user: user_dependency, db: db_dependency, phone_number: str):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    user_model.phone_number = phone_number
    db.commit()

```

---

### 🔎 ASCII Visual

```
Before: user could only save → email, name, password
After:  user can also save → phone_number

```

---

✅ Done! Now your database + application both support phone numbers 🎉

---

Would you like me to also make a **full start-to-end flow diagram** (ASCII) showing how we went from Step 1 → Step 9?

---

# Alembic Migration Full Flow

```
STEP 1: What is Alembic?
   └── Alembic = tool to change database schema without losing data

STEP 2: Install Alembic
   └── pip install alembic

STEP 3: Initialize Alembic Project
   └── alembic init alembic
       ├── alembic.ini   (config file)
       └── alembic/      (stores migration scripts)

STEP 4: Configure Files
   ├── alembic.ini  → add database URL
   └── env.py       → link Alembic with models.py

STEP 5: Create Revision (like git commit)
   └── alembic revision -m "add phone number"
       └── creates empty upgrade() + downgrade() file

STEP 6: Write Migration Code
   ├── upgrade()   → add phone_number column
   └── downgrade() → remove phone_number column

STEP 7: Run Upgrade
   └── alembic upgrade head
       └── DB now has phone_number column

STEP 8: Run Downgrade
   └── alembic downgrade -1
       └── undo last migration (remove phone_number)

STEP 9: Update Application
   ├── models.py  → add phone_number = Column(String)
   ├── schemas    → add phone_number to CreateUserRequest
   ├── auth.py    → save phone_number on user creation
   └── users.py   → add endpoint to change phone_number

```

---

# Visual Timeline

```
[DB Schema] ----(SQLAlchemy only)----> cannot change tables
     |
     v
 [Alembic] ----> create revisions (like git commits)
     |
     v
 upgrade() → adds new things
 downgrade() → removes things
     |
     v
 [Application Code Updated] → models + APIs now use new column

```

---
