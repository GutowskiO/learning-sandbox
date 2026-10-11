package org.gutenn.trollplugin;

import org.bukkit.plugin.java.JavaPlugin;
import org.gutenn.trollplugin.commands.WorldSpawnCommand;
import org.gutenn.trollplugin.listeners.PlayerJoinListener;

public final class TrollPlugin extends JavaPlugin {

    @Override
    public void onEnable() {

        if (!getDataFolder().exists()) {
            getLogger().info("Creating " + getDataFolder() + " main directory ");
            getDataFolder().mkdir();
        }
        saveDefaultConfig();

        getServer().getPluginManager().registerEvents(new PlayerJoinListener(), this);
        getCommand("setwspawn").setExecutor(new WorldSpawnCommand(this));

    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }
}
