"use client";

import dynamic from "next/dynamic";

// Firebase auth is browser-only; skip SSR to avoid prerender errors when
// env vars aren't set at build time.
const AuthButton = dynamic(() => import("./AuthButton"), { ssr: false });

export default AuthButton;
