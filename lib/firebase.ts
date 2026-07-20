import { initializeApp, getApps, getApp, type FirebaseApp } from "firebase/app";
import { getAuth, type Auth } from "firebase/auth";

// Only initialize Firebase if the API key is actually configured.
// Without this guard, Firebase 12 throws auth/invalid-api-key synchronously
// at module-load time when the env vars are missing, crashing the React root.
// Auth is optional — the site works fully without it.
const apiKey = process.env.NEXT_PUBLIC_FIREBASE_API_KEY;

let _app: FirebaseApp | null = null;
let _auth: Auth | null = null;

if (apiKey) {
  _app = getApps().length === 0
    ? initializeApp({
        apiKey,
        authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
        projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
        appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
      })
    : getApp();
  _auth = getAuth(_app);
}

export const auth: Auth | null = _auth;
