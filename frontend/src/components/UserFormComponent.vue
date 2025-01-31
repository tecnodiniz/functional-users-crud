<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon="mdi-plus-circle"
        text="Add User"
        variant="plain"
        v-bind="activatorProps"
      ></v-btn>
    </template>

    <v-card prepend-icon="mdi-account" title="New User">
      <v-card-text>
        <v-form v-model="form.valid">
          <v-row dense>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.username"
                hint="User Name"
                label="User Name*"
                required
                :rules="[form.rule.nameRules]"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.password"
                label="Password*"
                type="password"
                required
                :rules="[form.rule.pwdRules]"
                @keyup.enter="emitUser"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="12">
              <v-select
                :items="timezones"
                label="Timezone*"
                v-model="form.preferences.timezone"
                :rules="[form.rule.required]"
              >
              </v-select>
            </v-col>

            <v-col cols="12" sm="6">
              <label for="role">Roles</label>
              <v-checkbox
                v-for="(role, index) in availableRoles"
                :v-model="form.roles"
                :key="index"
                :value="role"
                :label="role"
                required
                density="compact"
                hide-details
              >
              </v-checkbox>
            </v-col>

            <v-col cols="12" sm="6">
              <label for="active">Is Active?</label>
              <v-radio-group v-model="form.active" name="active">
                <v-radio label="Active" :value="true"></v-radio>
                <v-radio label="Inactive" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
          </v-row>
        </v-form>
        <slot></slot>

        <small class="text-caption text-medium-emphasis">*indicates required field</small>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

        <v-btn
          :disabled="!form.valid"
          color="primary"
          text="Sign in"
          variant="tonal"
          @click="emitUser"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref } from 'vue'
const dialog = ref(false)

const emit = defineEmits(['new-user'])
const availableRoles = ref(['admin', 'manager', 'tester'])
const timezones = ref(Intl.supportedValuesOf('timeZone'))
const form = ref({
  valid: false,
  username: '',
  password: '',
  roles: [],
  active: false,
  preferences: {
    timezone: '',
  },
  rule: {
    nameRules: (value) => {
      if (!value) return 'Name is required'
      if (value?.length < 2) return 'Name must have at least 2 caracters'
      return true
    },
    pwdRules: (value) => {
      if (!value) return 'Password is required'
      if (value?.length < 6) return 'Name must have at least 6 caracters'
      return true
    },
    required: (v) => !!v || 'Field is required',
  },
})

const emitUser = () => {
  if (form.value.valid) {
    const payload = {
      username: form.value.username,
      roles: form.value.roles,
      active: form.value.active,
      password: form.value.password,
      preferences: {
        timezone: form.value.preferences.timezone,
      },
    }
    dialog.value = false

    form.value.username = ''
    form.value.login = ''
    form.value.password = ''
    form.value.roles = []
    form.value.active = false
    form.value.preferences.timezone = ''

    emit('new-user', payload)
  }
}
</script>
