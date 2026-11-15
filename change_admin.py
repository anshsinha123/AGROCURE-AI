"""
AgroCure AI - Administrator Management & Password Reset Utility
Use this script to view, add, edit, or reset any administrator credentials.
"""

import sys
import json
import hashlib
import time
import argparse
from datetime import datetime
from pathlib import Path

SALT = "agrocure_salt_2026"

PATHS = [Path(__file__).resolve().parent / "data" / "admins.json"]

def hash_pw(pw: str) -> str:
    return hashlib.sha256((pw + SALT).encode("utf-8")).hexdigest()

def load_admins(file_path: Path):
    if not file_path.exists():
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_admins(file_path: Path, data):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def list_admins():
    admins = load_admins(PATHS[0])
    print("\n--- Current Registered AgroCure AI Administrators ---")
    for idx, a in enumerate(admins, 1):
        print(f"[{idx}] ID:         {a.get('id')}")
        print(f"    Name:       {a.get('name')}")
        print(f"    Email:      {a.get('email')}")
        print(f"    Role:       {a.get('role')}")
        print(f"    Department: {a.get('department')}")
        print(f"    Status:     {a.get('status')}")
        print(f"    Last Login: {a.get('last_login', 'Never')}")
        print("-" * 48)
    print()

def add_admin(name: str, email: str, password: str, role: str = "Admin", dept: str = "Agricultural Operations"):
    if not name or not email or not password:
        print("[ERROR] --name, --email, and --password are required to add an administrator.")
        return

    email = email.strip().lower()
    role_formatted = "Super Admin" if "super" in role.lower() else ("Content Manager" if "content" in role.lower() else "Admin")

    new_admin = {
        "id": f"adm_{int(time.time())}",
        "name": name.strip(),
        "email": email,
        "password_hash": hash_pw(password),
        "role": role_formatted,
        "avatar": "/static/team/dev1.png",
        "department": dept.strip() if dept else "Agricultural Operations",
        "status": "Active",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_login": "Never"
    }

    for p in PATHS:
        admins = load_admins(p)
        # Check if email exists
        if any(a.get("email", "").lower() == email for a in admins):
            print(f"[ERROR] An administrator with email '{email}' already exists in {p}.")
            return
        admins.append(new_admin)
        save_admins(p, admins)
        print(f"Added '{name}' ({role_formatted}) to {p}")

    print(f"\n[SUCCESS] Administrator '{name}' successfully added with role '{role_formatted}'!")

def update_admin(target_email: str, new_name: str = None, new_email: str = None, new_password: str = None, new_role: str = None, new_dept: str = None):
    success = False
    for p in PATHS:
        admins = load_admins(p)
        matched = False
        for a in admins:
            if a.get("email", "").lower() == target_email.lower():
                matched = True
                if new_name:
                    a["name"] = new_name.strip()
                if new_email:
                    a["email"] = new_email.strip().lower()
                if new_password:
                    a["password_hash"] = hash_pw(new_password)
                if new_role:
                    role_fmt = "Super Admin" if "super" in new_role.lower() else ("Content Manager" if "content" in new_role.lower() else "Admin")
                    a["role"] = role_fmt
                if new_dept:
                    a["department"] = new_dept.strip()
                break
        if matched:
            save_admins(p, admins)
            success = True
            print(f"Updated administrator record in: {p}")
        else:
            print(f"Warning: Admin with email '{target_email}' not found in {p}")

    if success:
        print("\n[SUCCESS] Administrator details updated successfully!")
    else:
        print(f"\n[ERROR] No administrator found matching '{target_email}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AgroCure AI Administrator Management Utility")
    parser.add_argument("--list", action="store_true", help="List all registered administrators")
    parser.add_argument("--add", action="store_true", help="Add a new administrator")
    parser.add_argument("--target", type=str, help="Target admin email to edit; required when updating an administrator")
    parser.add_argument("--name", type=str, help="Admin full name")
    parser.add_argument("--email", type=str, help="Admin email address")
    parser.add_argument("--password", type=str, help="Admin plaintext password")
    parser.add_argument("--role", type=str, help="Admin role: 'Super Admin', 'Admin', or 'Content Manager'", default="Admin")
    parser.add_argument("--dept", type=str, help="Department or Title", default="Technical Operations")

    args = parser.parse_args()

    if args.add:
        add_admin(name=args.name, email=args.email, password=args.password, role=args.role, dept=args.dept)
    elif args.list or (len(sys.argv) == 1):
        list_admins()
        print("Usage Examples:")
        print("  1. List all admins:")
        print("     python change_admin.py --list\n")
        print("  2. Add a new admin:")
        print('     python change_admin.py --add --name "John Doe" --email "john@example.com" --password "replace-with-a-private-password" --role "Admin"\n')
        print("  3. Change existing admin details:")
        print('     python change_admin.py --target admin@example.com --name "My New Name"\n')
        print("  4. Reset admin password:")
        print('     python change_admin.py --target admin@example.com --password "replace-with-a-private-password"\n')
    else:
        if not args.target:
            parser.error("--target is required when updating an administrator.")
        update_admin(
            target_email=args.target,
            new_name=args.name,
            new_email=args.email,
            new_password=args.password,
            new_role=args.role,
            new_dept=args.dept
        )
