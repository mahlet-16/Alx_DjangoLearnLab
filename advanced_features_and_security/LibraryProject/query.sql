BEGIN;
--
-- Create model Book
--
CREATE TABLE "bookshelf_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "author" varchar(100) NOT NULL, "publication_year" integer NOT NULL);
--
-- Create model CustomUser
--
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "date_of_birth" date NOT NULL, "profile_pic" varchar(100) NOT NULL);
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Review
--
CREATE TABLE "bookshelf_review" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "review_text" text NOT NULL, "created_at" datetime NOT NULL, "book_id" bigint NOT NULL REFERENCES "bookshelf_book" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "auth_user_groups_customuser_id_group_id_3c656da4_uniq" ON "auth_user_groups" ("customuser_id", "group_id");
CREATE INDEX "auth_user_groups_customuser_id_62675d7c" ON "auth_user_groups" ("customuser_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_customuser_id_permission_id_f01ff6bf_uniq" ON "auth_user_user_permissions" ("customuser_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_customuser_id_843d9bac" ON "auth_user_user_permissions" ("customuser_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "bookshelf_review_book_id_abcbe232" ON "bookshelf_review" ("book_id");
CREATE INDEX "bookshelf_review_user_id_ff5193d5" ON "bookshelf_review" ("user_id");
COMMIT;
