<template>
  <div v-if="!isEditable" class="user-detail-container">
    <h1>User Details</h1>
    <table class="table table-striped mb-2">
      <tbody>
        <tr>
          <th>_id</th>
          <td>{{ user._id }}</td>
        </tr>
        <tr>
          <th>Username</th>
          <td>{{ user.username }}</td>
        </tr>
        <tr>
          <th>Active</th>
          <td>{{ user.active ? "Yes" : "No" }}</td>
        </tr>
        <tr>
          <th>Created At</th>
          <td>{{ formatDate(user.created_ts) }}</td>
        </tr>
        <tr>
          <th>Updated At</th>
          <td>{{ user.updated_ts ? formatDate(user.updated_ts) : '' }}</td>
        </tr>
        <tr>
          <th>Password</th>
          <td>{{ user.password }}</td>
        </tr>
        <tr>
          <th>Preferences</th>
          <td>{{ user.preferences.timezone }}</td>
        </tr>
        <tr>
          <th>Roles</th>
          <td>{{ user.roles.join(", ") }}</td>
        </tr>
      </tbody>
    </table>

    <div class="flex mt-2">
      <router-link :to="`/`">
          <v-btn
            color="primary mb-4"
          >
            Go Back
          </v-btn>
      </router-link>
      
      <router-link :to="`/user/${user._id}?isEditable=true`">
          <v-btn
            color="primary mb-4"
          >
            Edit
            <i class="bi bi-pencil-square"></i>
          </v-btn>
      </router-link>

      </div>
    
  </div>

  <div v-if="isEditable">
    <EditUserForm :id="this.$route.params.id" />
  </div>
</template>

<script>
import EditUserForm from '@/components/editUserForm/EditUserForm.vue';
import { get_user } from '@/services/api';

export default {
  name: "UserDetailPage",
  components:{
    EditUserForm
  },
  props:{
    id:{
      type: String,
      required: true
    }
  },
  data() {
    return {
      user: {
        _id: "",
        username: "",
        active: false,
        created_ts: 0,
        password: "",
        preferences: {
          timezone: "",
        },
        roles: [],
      },
    };
  },
  computed: {
    // Accesses the isEditable value of the route query
    isEditable() {
      return this.$route.query.isEditable === 'true'; // Compares the query as string
    }
  },

  methods: {
    goBack(){
    this.$router.push('/'); 
    
  },
    // Format Date
    formatDate(timestamp) {
      const date = new Date(timestamp * 1000); // Converts from seconds to milliseconds
      return date.toLocaleString("en-US", { timeZone: this.user.preferences.timezone || "UTC" });
    },

    getUserDetails() {
      get_user(this.$route.params.id)
        .then((response) => {
          this.user = response.data.user; // Setting user
          console.log(this.user);
        })
        .catch((error) => console.error("Erro ao buscar detalhes do usuário:", error));
    },
  },

  created() {
    this.getUserDetails();
  },
};
</script>

<style scoped>
.flex{
  display: flex;
  justify-content: space-evenly;
}
.user-detail-container {
  padding: 20px;
}

h1 {
  margin-bottom: 20px;
}

.table {
  width: 100%;
  max-width: 600px;
  margin: auto;
}
</style>
