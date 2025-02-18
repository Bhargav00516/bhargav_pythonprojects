import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.util.HashMap;
import java.util.Map;

class BankAccount {
    private String accountHolder;
    private double balance;
    private String accountNumber;

    public BankAccount(String accountHolder, double initialBalance, String accountNumber) {
        this.accountHolder = accountHolder;
        this.balance = initialBalance;
        this.accountNumber = accountNumber;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            JOptionPane.showMessageDialog(null, "₹" + amount + " deposited successfully.");
        } else {
            JOptionPane.showMessageDialog(null, "Invalid deposit amount!", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            JOptionPane.showMessageDialog(null, "₹" + amount + " withdrawn successfully.");
        } else {
            JOptionPane.showMessageDialog(null, "Insufficient balance or invalid amount!", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public double getBalance() {
        return balance;
    }

    public String getAccountHolder() {
        return accountHolder;
    }

    public String getAccountNumber() {
        return accountNumber;
    }
}

public class BankManagementGUI extends JFrame {
    private static int accountCounter = 1000; // Starting account number
    private static Map<String, BankAccount> accounts = new HashMap<>(); // Store accounts dynamically

    private JLabel balanceLabel;
    private JTextField amountField;
    private JTextField accountNumberField;

    public BankManagementGUI() {
        // Window settings
        setTitle("Bank Management System");
        setSize(400, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(7, 1, 5, 5));

        // Account Number input field with placeholder
        accountNumberField = new JTextField("Enter Account No");
        accountNumberField.setHorizontalAlignment(JTextField.CENTER);
        accountNumberField.setForeground(Color.LIGHT_GRAY);  // Light gray color for placeholder text
        accountNumberField.addFocusListener(new FocusListener() {
            public void focusGained(FocusEvent e) {
                if (accountNumberField.getText().equals("Enter Account No")) {
                    accountNumberField.setText("");
                    accountNumberField.setForeground(Color.BLACK); // Dark color when user starts typing
                }
            }

            public void focusLost(FocusEvent e) {
                if (accountNumberField.getText().equals("")) {
                    accountNumberField.setText("Enter Account No");
                    accountNumberField.setForeground(Color.LIGHT_GRAY); // Light gray when it's empty
                }
            }
        });
        add(accountNumberField);

        // Balance label
        balanceLabel = new JLabel("Current Balance: ₹0.00", JLabel.CENTER);
        add(balanceLabel);

        // Amount input field with placeholder
        amountField = new JTextField("Enter Amount");
        amountField.setHorizontalAlignment(JTextField.CENTER);
        amountField.setForeground(Color.LIGHT_GRAY);  // Light gray color for placeholder text
        amountField.addFocusListener(new FocusListener() {
            public void focusGained(FocusEvent e) {
                if (amountField.getText().equals("Enter Amount")) {
                    amountField.setText("");
                    amountField.setForeground(Color.BLACK); // Dark color when user starts typing
                }
            }

            public void focusLost(FocusEvent e) {
                if (amountField.getText().equals("")) {
                    amountField.setText("Enter Amount");
                    amountField.setForeground(Color.LIGHT_GRAY); // Light gray when it's empty
                }
            }
        });
        add(amountField);

        // Create Account button
        JButton createAccountButton = new JButton("Create Account");
        createAccountButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String accountHolder = JOptionPane.showInputDialog("Enter Account Holder's Name:");
                String accountNumber = "AC" + accountCounter++; // Generate dynamic account number
                BankAccount newAccount = new BankAccount(accountHolder, 0, accountNumber);
                accounts.put(accountNumber, newAccount);

                accountNumberField.setText(accountNumber); // Display generated account number
                JOptionPane.showMessageDialog(null, "Account Created! Account Number: " + accountNumber);
            }
        });
        add(createAccountButton);

        // Deposit button
        JButton depositButton = new JButton("Deposit");
        depositButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String accountNumber = accountNumberField.getText();
                BankAccount account = accounts.get(accountNumber);
                if (account != null) {
                    try {
                        double amount = Double.parseDouble(amountField.getText());
                        account.deposit(amount);
                        updateBalance(account);
                    } catch (NumberFormatException ex) {
                        JOptionPane.showMessageDialog(null, "Enter a valid amount!", "Error", JOptionPane.ERROR_MESSAGE);
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Account not found.", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        add(depositButton);

        // Withdraw button
        JButton withdrawButton = new JButton("Withdraw");
        withdrawButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String accountNumber = accountNumberField.getText();
                BankAccount account = accounts.get(accountNumber);
                if (account != null) {
                    try {
                        double amount = Double.parseDouble(amountField.getText());
                        account.withdraw(amount);
                        updateBalance(account);
                    } catch (NumberFormatException ex) {
                        JOptionPane.showMessageDialog(null, "Enter a valid amount!", "Error", JOptionPane.ERROR_MESSAGE);
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Account not found.", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        add(withdrawButton);

        // Check Balance button
        JButton balanceButton = new JButton("Check Balance");
        balanceButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String accountNumber = accountNumberField.getText();
                BankAccount account = accounts.get(accountNumber);
                if (account != null) {
                    JOptionPane.showMessageDialog(null, "Current Balance: ₹" + account.getBalance(), "Balance Info", JOptionPane.INFORMATION_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(null, "Account not found.", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        add(balanceButton);
    }

    private void updateBalance(BankAccount account) {
        balanceLabel.setText("Current Balance: ₹" + account.getBalance());
        amountField.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BankManagementGUI gui = new BankManagementGUI();
            gui.setVisible(true);
        });
    }
}
