CREATE DATABASE gambler_db;
USE gambler_db;

CREATE TABLE gambler_profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    initial_stake DOUBLE,
    current_stake DOUBLE,
    win_threshold DOUBLE,
    loss_threshold DOUBLE,
    total_bets INT DEFAULT 0,
    total_wins INT DEFAULT 0,
    total_losses INT DEFAULT 0,
    total_winnings DOUBLE DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE stake_transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gambler_id INT,
    transaction_type VARCHAR(50),
    amount DOUBLE,
    balance_after DOUBLE,
    bet_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gambler_id) REFERENCES gambler_profile(id)
);