import { BACKEND_URL, API_KEY } from "$env/static/private";

export async function isBackendRunning(): Promise<boolean> {
  try {
    const resp = await fetch(BACKEND_URL + "/ping", {
      headers: { "Authorization": "Bearer " + API_KEY }
    });

    if (!resp.ok) {
      return false;
    }
    return true; 
  } catch (e: any) {
    return false;
  }
}
