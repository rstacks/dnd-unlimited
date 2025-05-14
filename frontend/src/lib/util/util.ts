export function closeModal(modalId: string): void {
  const modalElement = document.getElementById(modalId);
  if (!modalElement) {
    return;
  }
  const modal = modalElement as HTMLInputElement;
  modal.checked = false;
}
