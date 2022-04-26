-- upgrade --
CREATE TABLE IF NOT EXISTS "jokes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "setup" TEXT NOT NULL,
    "punchline" TEXT NOT NULL,
    "type" VARCHAR(15) NOT NULL
);
COMMENT ON TABLE "jokes" IS 'The Joke model';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
