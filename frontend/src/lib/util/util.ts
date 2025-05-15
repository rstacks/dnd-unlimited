export function closeModal(modalId: string): void {
  const modalElement = document.getElementById(modalId);
  if (!modalElement) {
    return;
  }
  const modal = modalElement as HTMLInputElement;
  modal.checked = false;
}

export function isIosBrowser(): boolean {
  /**
   * Type "any" because "standalone" property only exists on Safari iOS.
   * TS does not recognize it as a standard property.
   */
  const navigator: any = window.navigator;
  if (navigator.standalone !== undefined && !(navigator.standalone)) {
    return true;
  }
  return false;
}
