CREATE TYPE account_type AS ENUM (
    'ASSET',
    'LIABILITY',
    'INCOME',
    'EXPENSE'
);

CREATE TABLE accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    name VARCHAR(100) NOT NULL,
    type account_type NOT NULL,
    currency VARCHAR(3) DEFAULT 'INR',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE journal_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    description TEXT,
    transaction_date TIMESTAMP WITH TIME ZONE NOT NULL,
    source VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE journal_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    journal_entry_id UUID NOT NULL REFERENCES journal_entries(id) ON DELETE CASCADE,
    account_id UUID NOT NULL REFERENCES accounts(id),
    amount NUMERIC(15, 2) NOT NULL,
    reimbursement_status BOOLEAN DEFAULT FALSE,
    tax_deductible_section VARCHAR(20)
);

CREATE INDEX idx_accounts_user ON accounts(user_id);
CREATE INDEX idx_journal_entries_user_date ON journal_entries(user_id, transaction_date DESC);
CREATE INDEX idx_journal_lines_account ON journal_lines(account_id);
