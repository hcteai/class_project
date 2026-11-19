class GroupService:
    MAX_GROUP_NAME_LENGTH = 50

    def __init__(self, group_storage, note_storage):
        self._groups = group_storage
        self._notes = note_storage

    def create_group(self, name):
        """Create a uniquely named group for notes."""
        self._check_group_name(name)
        normalized_name = name.strip()
        if any(g.name == normalized_name for g in self._groups.get_all()):
            raise ValueError(f"Group '{normalized_name}' already exists.")
        return self._groups.add(normalized_name)

    def get_all_groups(self):
        return self._groups.get_all()

    def find_group(self, group_id):
        group = self._groups.get(group_id)
        if group is None:
            raise ValueError(f"Group {group_id} not found.")
        return group

    def delete_group(self, group_id):
        if not self._groups.delete(group_id):
            raise ValueError(f"Group {group_id} not found.")

    def add_note(self, group_id, note_id):
        group = self.find_group(group_id)
        if self._notes.get(note_id) is None:
            raise ValueError(f"Note {note_id} not found.")
        if not group.add_note(note_id):
            raise ValueError(f"Note {note_id} is already in group {group_id}.")
        return group

    def remove_note(self, group_id, note_id):
        group = self.find_group(group_id)
        if not group.remove_note(note_id):
            raise ValueError(f"Note {note_id} is not in group {group_id}.")
        return group

    def get_group_notes(self, group_id):
        group = self.find_group(group_id)
        notes = (self._notes.get(note_id) for note_id in group.note_ids)
        return [note for note in notes if note is not None]

    def _check_group_name(self, name):
        if not name or not name.strip():
            raise ValueError("Group name is required.")
        if len(name.strip()) > self.MAX_GROUP_NAME_LENGTH:
            raise ValueError(
                f"Group name must be at most {self.MAX_GROUP_NAME_LENGTH} characters."
            )
