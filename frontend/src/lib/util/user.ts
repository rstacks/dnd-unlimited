import { BACKEND_URL } from "$env/static/private";
import { error } from "@sveltejs/kit";
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
  const resp = await fetch(BACKEND_URL + "/users");
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
    const nextSessionId = user.session_uuid;
    if (sessionId === nextSessionId) {
      return user.id;
    }
  }
  return -1;
}

export async function getUserById(userId: number): Promise<UserData> {
  const resp = await fetch(BACKEND_URL + "/users/" + userId);
  if (resp.status === 404) {
    error(404, { message: "User not found" });
  } else if (!resp.ok) {
    error(503, { message: "Server offline" });
  }

  const userData: UserData = await resp.json();
  return userData;
}
