CREATE DATABASE IF NOT EXISTS vet_auth;
CREATE DATABASE IF NOT EXISTS appointments_db;

-- Cambia de base
USE appointments_db;

-- Crea tablas
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_name VARCHAR(255) NOT NULL,
    owner_name VARCHAR(255) NOT NULL,
    date DATETIME NOT NULL,
    reason VARCHAR(255) DEFAULT NULL
);

USE vet_auth;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) DEFAULT NULL,
    role ENUM('owner', 'admin') DEFAULT 'owner' NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- 🔑 Da permisos al usuario 'user' (definido en docker-compose)
GRANT ALL PRIVILEGES ON vet_auth.* TO 'user'@'%';
GRANT ALL PRIVILEGES ON appointments_db.* TO 'user'@'%';
FLUSH PRIVILEGES;
