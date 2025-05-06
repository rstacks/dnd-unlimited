import { BACKEND_URL, API_KEY } from "$env/static/private";
import { error, type Cookies } from "@sveltejs/kit";
import bcrypt from "bcrypt";

interface UserAuthInfo {
  id: number;
  phone_hash: string;
  session_uuid: string;
}

interface UserData {
  phone_hash: string;
  user_type: string;
  user_name: string;
  session_uuid: string;
}

interface UsersJSON {
  users: UserAuthInfo[];
}

export async function fetchUsers(): Promise<UserAuthInfo[]> {
  const resp = await fetch(BACKEND_URL + "/users", {
    headers: { "Authorization": "Bearer " + API_KEY }
  });
  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
  const usersJson: UsersJSON = await resp.json();
  const allUsers = usersJson.users;
  return allUsers;
}

export async function getUserIdByPhone(phonePlaintext: string): Promise<number> {
  const allUsers = await fetchUsers();
  for (const user of allUsers) {
    const nextPhoneHash = user.phone_hash;
    const userExists = await bcrypt.compare(phonePlaintext, nextPhoneHash);
    if (userExists) {
      return user.id;
    }
  }
  return -1;
}

export async function getUserIdBySession(sessionId: string): Promise<number> {
  const allUsers = await fetchUsers();
  for (const user of allUsers) {
    const nextSessionIdHash = user.session_uuid;
    const userExists = await bcrypt.compare(sessionId, nextSessionIdHash);
    if (userExists) {
      return user.id;
    }
  }
  return -1;
}

export async function getUserById(userId: number): Promise<UserData> {
  const resp = await fetch(BACKEND_URL + "/users/" + userId, {
    headers: { "Authorization": "Bearer " + API_KEY }
  });
  if (resp.status === 404) {
    error(404, { message: "User not found" });
  } else if (!resp.ok) {
    error(503, { message: "Server offline" });
  }

  const userData: UserData = await resp.json();
  return userData;
}

export async function isLoggedIn(cookies: Cookies): Promise<boolean> {
  const sessionId = cookies.get("sessionId");
  if (!sessionId) {
    return false;
  }
  const userId = await getUserIdBySession(sessionId);
  if (userId === -1) {
    return false;
  }

  return true;
}
