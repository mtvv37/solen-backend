-- Audit V0: free conversion audits and the emails left to unlock them.
-- RLS is enabled with no policies: only the server (service-role key) can read or write.

create table if not exists public.audits (
  id            text primary key check (id ~ '^[A-Za-z0-9_-]{22}$'),
  created_at    timestamptz not null default now(),
  ip_hash       text not null,
  url           text not null,
  shop_domain   text not null,
  product_url   text not null,
  product_name  text,
  is_shopify    boolean not null default false,
  score         smallint not null check (score between 0 and 100),
  categories    jsonb not null,
  checks        jsonb not null,
  summary       text not null,
  leaks         jsonb not null,
  assumptions   jsonb not null,
  writer        text not null default 'template'
);

create index if not exists audits_shop_domain_idx on public.audits (shop_domain);

create table if not exists public.audit_leads (
  id               uuid primary key default gen_random_uuid(),
  created_at       timestamptz not null default now(),
  audit_id         text not null references public.audits (id) on delete cascade,
  email            text not null check (char_length(email) <= 254),
  consent          boolean not null check (consent),
  consent_text     text not null,
  consent_version  text not null,
  consented_at     timestamptz not null,
  ip_hash          text not null
);

create index if not exists audit_leads_ip_hash_created_at_idx on public.audit_leads (ip_hash, created_at desc);
create index if not exists audit_leads_email_idx on public.audit_leads (lower(email));

-- Every audit request, successful or not, for per-IP rate limiting.
create table if not exists public.audit_attempts (
  id          bigint generated always as identity primary key,
  created_at  timestamptz not null default now(),
  ip_hash     text not null
);
create index if not exists audit_attempts_ip_hash_created_at_idx on public.audit_attempts (ip_hash, created_at desc);

alter table public.audits enable row level security;
alter table public.audit_attempts enable row level security;
alter table public.audit_leads enable row level security;
-- No policies on purpose: anon and authenticated roles get no access.
revoke all on public.audits from anon, authenticated;
revoke all on public.audit_leads from anon, authenticated;
revoke all on public.audit_attempts from anon, authenticated;
